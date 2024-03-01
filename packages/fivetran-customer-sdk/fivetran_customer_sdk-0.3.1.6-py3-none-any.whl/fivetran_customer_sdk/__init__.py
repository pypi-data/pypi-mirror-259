import docker
import grpc
import inspect
import json
import os
import requests as rq

from concurrent import futures
from datetime import datetime
from docker.types import Mount
from google.protobuf import timestamp_pb2

from fivetran_customer_sdk.protos import common_pb2
from fivetran_customer_sdk.protos import connector_sdk_pb2
from fivetran_customer_sdk.protos import connector_sdk_pb2_grpc

TESTER_IMAGE_NAME = "fivetrandocker/sdk-connector-tester"
TESTER_IMAGE_VERSION = "024.0222.001"
TESTER_CONTAINER_NAME = "fivetran_connector_tester"

BUILDER_IMAGE_NAME = "azul/zulu-openjdk"
BUILDER_IMAGE_VERSION = "17.0.8.1-17.44.53"
BUILDER_CONTAINER_NAME = "fivetran_connector_builder"

DEBUGGING = False


def upsert(table: str, data: dict, schema: str = None):
    __yield_check(inspect.stack())

    mapped_data = {}
    for k, v in data.items():
        if isinstance(v, int):
            mapped_data[k] = common_pb2.ValueType(int=v)
        elif isinstance(v, str):
            try:
                # Is it datetime?
                dt = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S%z")
                timestamp = timestamp_pb2.Timestamp()
                timestamp.FromDatetime(dt)
                mapped_data[k] = common_pb2.ValueType(utc_datetime=timestamp)
                continue
            except ValueError:
                pass

            mapped_data[k] = common_pb2.ValueType(string=v)
        else:
            print(f"WARNING: Unsupported data type in `{table}.{k}`, converting to STRING")
            mapped_data[k] = common_pb2.ValueType(string=str(v))

    record = connector_sdk_pb2.Record(
        schema_name=schema if schema else None,
        table_name=table,
        type="UPSERT",
        data=mapped_data
    )

    return connector_sdk_pb2.UpdateResponse(
        operation=connector_sdk_pb2.Operation(record=record))


def update(table: str, modified: dict, schema_name: str = None):
    __yield_check(inspect.stack())
    # TODO


def delete(table: str, primary_key: set, schema_name: str = None):
    __yield_check(inspect.stack())
    # TODO


def truncate(table: str, schema_name: str = None):
    __yield_check(inspect.stack())
    # TODO


def checkpoint(state: dict):
    __yield_check(inspect.stack())
    return connector_sdk_pb2.UpdateResponse(
             operation=connector_sdk_pb2.Operation(checkpoint=connector_sdk_pb2.Checkpoint(
                 state_json=json.dumps(state))))


def __yield_check(stack):
    # Known issue with inspect.getmodule() and yield behavior in a frozen application.
    # When using inspect.getmodule() on stack frames obtained by inspect.stack(), it fails
    # to resolve the modules in a frozen application due to incompatible assumptions about
    # the file paths. This can lead to unexpected behavior, such as yield returning None or
    # the failure to retrieve the module inside a frozen app
    # (Reference: https://github.com/pyinstaller/pyinstaller/issues/5963)
    if not DEBUGGING:
        return

    called_method = stack[0].function
    calling_code = stack[1].code_context[0]
    if f"{called_method}(" in calling_code:
        if 'yield' not in calling_code:
            print(f"ERROR: Please add 'yield' to '{called_method}' operation on line {stack[1].lineno} in file '{stack[1].filename}'")
            os._exit(1)
    else:
        # This should never happen
        raise RuntimeError(f"Unable to find '{called_method}' function in stack")


class Connector(connector_sdk_pb2_grpc.ConnectorServicer):
    def __init__(self, update, schema=None):
        self.schema_method = schema
        self.update_method = update

        self.configuration = None
        self.state = None
        self.tables = {}

    # Call this method to deploy the connector to Fivetran platform
    def deploy(self, project_path: str, deploy_key: str, group: str, connector: str, configuration: dict = None):
        if not deploy_key: print("ERROR: Missing deploy key"); os._exit(1)
        if not connector: print("ERROR: Missing connector name"); os._exit(1)
        secrets_list = []
        payloads_list = []
        if configuration:
            if any([key != "secrets" and key != "payloads" for key in configuration.keys()]):
                print("ERROR: Configuration should have only 'secrets' and 'payloads' keys")
                os._exit(1)

            if "secrets" in configuration:
                for k, v in configuration['secrets'].items():
                    if not isinstance(v, str):
                        print("ERROR: Use only string values as secrets")
                        os._exit(1)
                    secrets_list.append({"key": k, "value": v})

            if "payloads" in configuration:
                for k, v in configuration['payloads'].items():
                    if not isinstance(v, str):
                        print("ERROR: Use only string values as payloads")
                        os._exit(1)
                    payloads_list.append({"key": k, "value": v})

        connector_config = {
            "schema": connector,
            "secrets_list": secrets_list,
            "sync_method": "DIRECT",
            "custom_payloads": payloads_list,
        }
        group_id, group_name = self.__get_group_info(group, deploy_key)
        print(f"Deploying '{project_path}' to '{group_name}/{connector}'")
        self.__write_run_py(project_path)
        # TODO: we need to do this step on the server (upload code instead)
        self.__create_standalone_binary(project_path)
        self.__upload(os.path.join(project_path, "dist", "__run"),
                      deploy_key,
                      group_id,
                      connector)
        connector_id = self.__get_connector_id(connector, group, group_id, deploy_key)
        if connector_id:
            print(f"Connector '{connector}' already exists in group '{group}', updating configuration .. ", end="", flush=True)
            self.__update_connector(connector_id, connector, group_name, connector_config, deploy_key)
            print("✓")
        else:
            response = self.__create_connector(deploy_key, group_id, connector_config)
            if response.ok:
                print(f"New connector with name '{connector}' created")
            else:
                print(f"ERROR: Failed to create new connector: {response.json()['message']}")
                os._exit(1)

    @staticmethod
    def __update_connector(id: str, name: str, group: str, config: dict, deploy_key: str):
        resp = rq.patch(f"https://api.fivetran.com/v1/connectors/{id}",
                        headers={"Authorization": f"Basic {deploy_key}"},
                        json={"config": config})

        if not resp.ok:
            print(f"ERROR: Unable to update connector '{name}' in group '{group}'")
            os._exit(1)

    @staticmethod
    def __get_connector_id(name: str, group: str, group_id: str, deploy_key: str):
        resp = rq.get(f"https://api.fivetran.com/v1/groups/{group_id}/connectors",
                      headers={"Authorization": f"Basic {deploy_key}"},
                      params={"schema": name})
        if not resp.ok:
            print(f"ERROR: Unable to fetch connector list in group '{group}'")
            os._exit(1)

        if resp.json()['data']['items']:
            return resp.json()['data']['items'][0]['id']

        return None

    @staticmethod
    def __create_connector(deploy_key: str, group_id: str, config: dict):
        response = rq.post(f"https://api.fivetran.com/v1/connectors",
                           headers={"Authorization": f"Basic {deploy_key}"},
                           json={
                                 "group_id": group_id,
                                 "service": "my_built",
                                 "config": config,
                                 "paused": "false",
                                 "run_setup_tests": "false",
                                 "sync_frequency": "360",
                           })
        return response

    @staticmethod
    def __create_standalone_binary(project_path: str):
        print("Preparing artifacts")
        print("1 of 7 .. ", end="", flush=True)
        docker_client = docker.from_env()
        image = f"{BUILDER_IMAGE_NAME}:{BUILDER_IMAGE_VERSION}"
        result = docker_client.images.list(image)
        if not result:
            # Pull the builder image if missing
            docker_client.images.pull(BUILDER_IMAGE_NAME, BUILDER_IMAGE_VERSION)

        for container in docker_client.containers.list(all=True):
            if container.name == BUILDER_CONTAINER_NAME:
                if container.status == "running":
                    print("ERROR: Another deploy process is running")
                    os._exit(1)

        container = None
        try:
            # TODO: Check responses in each step and look for "success" phrases
            container = docker_client.containers.run(
                image=image,
                name=BUILDER_CONTAINER_NAME,
                command="/bin/sh",
                mounts=[Mount("/myapp", project_path, read_only=False, type="bind")],
                tty=True,
                detach=True,
                working_dir="/myapp",
                remove=True)
            print("✓")

            print("2 of 7 .. ", end="", flush=True)
            resp = container.exec_run("apt-get update")
            print("✓")

            print("3 of 7 .. ", end="", flush=True)
            resp = container.exec_run("apt-get install -y python3-pip")
            print("✓")

            print("4 of 7 .. ", end="", flush=True)
            resp = container.exec_run("pip install pyinstaller")
            print("✓")

            print("5 of 7 .. ", end="", flush=True)
            resp = container.exec_run("pip install fivetran_customer_sdk")
            print("✓")

            print("6 of 7 .. ", end="", flush=True)
            if os.path.isfile(os.path.join(project_path, "requirements.txt")):
                resp = container.exec_run("pip install -r requirements.txt")
            print("✓")

            print("7 of 7 .. ", end="", flush=True)
            resp = container.exec_run("rm __run")
            resp = container.exec_run("pyinstaller --onefile --clean __run.py")
            print("✓")

            if not os.path.isfile(os.path.join(project_path, "dist", "__run")):
                print("Prep phase failed")
                os._exit(1)

        finally:
            if container:
                container.stop()

    @staticmethod
    def __upload(local_path: str, deploy_key: str, group_id: str, connector: str):
        print("Deploying .. ", end="", flush=True)
        response = rq.post(f"https://api.fivetran.com/v2/deploy/{group_id}/{connector}",
                           files={'file': open(local_path, 'rb')},
                           headers={"Authorization": f"Basic {deploy_key}"})
        if response.ok:
            print("✓")
        else:
            print("fail\nERROR: ", response.reason)

    @staticmethod
    def __write_run_py(project_path: str):
        with open(os.path.join(project_path, "__run.py"), "w") as fo:
            fo.writelines([
                "import sys\n",
                "from main import connector\n",
                "if len(sys.argv) == 3 and sys.argv[1] == '--port':\n",
                "   server = connector.run(port=int(sys.argv[2]))\n",
                "else:\n",
                "   server = connector.run()\n"
            ])

    @staticmethod
    def __get_group_info(group: str, deploy_key: str) -> tuple[str, str]:
        resp = rq.get("https://api.fivetran.com/v1/groups",
                      headers={"Authorization": f"Basic {deploy_key}"})

        if not resp.ok:
            print(f"ERROR: Unable to fetch list of groups, status code = {resp.status_code}")
            os._exit(1)

        # TODO: Do we need to implement pagination?
        groups = resp.json()['data']['items']
        if not groups:
            print("ERROR: No destinations defined in the account")
            os._exit(1)

        if len(groups) == 1:
            return groups[0]['id'], groups[0]['name']
        else:
            if not group:
                print("ERROR: Group name is required when there are multiple destinations in the account")
                os._exit(1)

            for grp in groups:
                if grp['name'] == group:
                    return grp['id'], grp['name']

        print(f"ERROR: Specified group was not found in the account: {group}")
        os._exit(1)

    # Call this method to run the connector in production
    def run(self, port: int = 50051, configuration: dict = None, state: dict = None) -> grpc.Server:
        global DEBUGGING
        self.configuration = configuration if configuration else {}
        self.state = state if state else {}

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        connector_sdk_pb2_grpc.add_ConnectorServicer_to_server(self, server)
        server.add_insecure_port("[::]:" + str(port))
        server.start()
        print("Connector started, listening on " + str(port))
        if DEBUGGING:
            return server
        server.wait_for_termination()

    # This method starts both the server and the local testing environment
    def debug(self, project_path: str = None, port: int = 50051, configuration: dict = None, state: dict = None) -> bool:
        global DEBUGGING
        DEBUGGING = True

        project_path = os.getcwd() if project_path is None else project_path
        print(f"Debugging connector: {project_path}")
        server = self.run(port, configuration, state)

        # Uncomment this to run the tester manually
        #server.wait_for_termination()

        docker_client = docker.from_env()
        image = f"{TESTER_IMAGE_NAME}:{TESTER_IMAGE_VERSION}"
        result = docker_client.images.list(image)
        if not result:
            # Pull the tester image if missing
            docker_client.images.pull(TESTER_IMAGE_NAME, TESTER_IMAGE_VERSION)

        error = False
        try:
            for container in docker_client.containers.list(all=True):
                if container.name == TESTER_CONTAINER_NAME:
                    if container.status == "running":
                        container.stop()
                    else:
                        container.remove()
                    break

            working_dir = os.path.join(project_path, "files")
            try:
                os.mkdir(working_dir)
            except FileExistsError:
                pass

            container = docker_client.containers.run(
                image=image,
                name=TESTER_CONTAINER_NAME,
                command="--custom-sdk=true",
                mounts=[Mount("/data", working_dir, read_only=False, type="bind")],
                network="host",
                remove=True,
                detach=True,
                environment=["GRPC_HOSTNAME=host.docker.internal"])

            for line in container.attach(stdout=True, stderr=True, stream=True):
                msg = line.decode("utf-8")
                print(msg, end="")
                if ("Exception in thread" in msg) or ("SEVERE:" in msg):
                    error = True

        finally:
            server.stop(grace=2.0)
            return not error

    # -- Methods below override ConnectorServicer methods
    def ConfigurationForm(self, request, context):
        if not self.configuration:
            self.configuration = {}

        # Not going to use the tester's configuration file
        return common_pb2.ConfigurationFormResponse()

    def Test(self, request, context):
        return None

    def Schema(self, request, context):
        if self.schema_method:
            response = self.schema_method(self.configuration)

            for entry in response:
                if 'table' not in entry:
                    print("ERROR: Entry missing table name: " + entry)
                    os._exit(1)

                table_name = entry['table']

                if table_name in self.tables:
                    print("ERROR: Table already defined: " + table_name)
                    os._exit(1)

                table = common_pb2.Table(name=table_name)
                columns = {}

                if "primary_key" not in entry:
                    print("ERROR: Table requires at least one primary key: " + table_name)
                    os._exit(1)

                for pkey_name in entry["primary_key"]:
                    column = columns[pkey_name] if pkey_name in columns \
                                                else common_pb2.Column(name=pkey_name)
                    column.primary_key = True
                    columns[pkey_name] = column

                if "columns" in entry:
                    for column_name in entry["columns"]:
                        column = columns[column_name] if column_name in columns \
                                                      else common_pb2.Column(name=column_name)

                        # TODO: Map column types entry['columns'][column_name] to common_pb2.Column

                        if column_name in entry["primary_key"]:
                            column.primary_key = True

                        columns[column_name] = column

                table.columns.extend(columns.values())
                self.tables[table_name] = table

            return connector_sdk_pb2.SchemaResponse(without_schema=common_pb2.TableList(tables=self.tables.values()))

        else:
            return connector_sdk_pb2.SchemaResponse(schema_response_not_supported=True)

    def Update(self, request, context):
        state = self.state if self.state else json.loads(request.state_json)

        try:
            for resp in self.update_method(configuration=self.configuration, state=state):
                yield resp
        except TypeError as e:
            if str(e) != "'NoneType' object is not iterable":
                raise e
