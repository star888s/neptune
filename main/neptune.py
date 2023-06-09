import json
import logging
import requests

# gremlin
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


# TODO リソースを立ててからresponseのkeyを各自調整する
class Neptune:
    def __init__(self, endpoint) -> None:
        self.endpoint = endpoint

        self.traversal = traversal().withRemote(
            DriverRemoteConnection(endpoint, "g", verify_ssl=False)
        )

        logging.info(f"query {endpoint}")

        return None

    # sample for low-level api
    def low_api(self, query: str) -> dict[str]:
        try:
            logging.info(f"Query : {query}")

            payload = json.dumps({"gremlin": query})

            response = requests.post(self.endpoint, data=payload, verify=False)

            logging.info(f"response result {response}")

            if response.status_code == 200:
                return {"status_code": response.status_code, "body": response.text}

            else:
                return {"status_code": response.status_code, "body": response.text}

        except BaseException:
            logging.critical("exception occurred")
            raise

    def put_node(self, item: str, properties: dict[str]) -> dict[str]:
        try:
            attr = ""

            for key, value in properties.items():
                attr += f".property({key},{value})"
            # TODO nextの調査
            query = f"""g.addV("{item}"){attr}.next()"""

            logging.info(f"Query : {query}")

            logging.info("Query Creation Completed")

            return self.low_api(query)

        except BaseException:
            logging.critical("exception occurred")
            raise

    def update_edge(self, item: str, properties: dict[str]) -> dict[str]:
        try:
            attr = ""

            for key, value in properties.items():
                attr += f".property({key},{value})"
            # TODO nextの調査
            query = f"""g.addV("{item}"){attr}.next()"""

            logging.info("Query Creation Completed")

            return self.low_api(query)

        except BaseException:
            logging.critical("exception occurred")
            raise
