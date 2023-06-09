import pytest
from requests import Response
import json
import logging

# module
from main import neptune

# gremlin
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


nep = neptune.Neptune(endpoint="hoge")


def mocked_request_post_200(*args, **kwargs):
    response = Response()
    response.status_code = 200
    return response


def mocked_request_post_400(*args, **kwargs):
    response = Response()
    response.status_code = 400
    return response


class TestNeptune:
    def test_low_api_200(self, mocker):
        with mocker.patch("requests.post", side_effect=mocked_request_post_200):
            result = nep.low_api(query="g.V().count()")

            assert result["status_code"] == 200

    def test_low_api_400(self, mocker):
        with mocker.patch("requests.post", side_effect=mocked_request_post_400):
            result = nep.low_api(query="g.V().count()")

            assert result["status_code"] == 400

    def test_put_node(self, mocker, caplog):
        with mocker.patch("requests.post", side_effect=mocked_request_post_200):
            caplog.set_level(logging.INFO)

            result = nep.put_node(item="1", properties={"name": "hoge", "name": "foo"})

            assert (
                'Query : g.addV("1").property(name,foo).next()'
                in caplog.record_tuples[2]
            )

            assert result["status_code"] == 200

    # def test_batch_put_node():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_upsert_node():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_update_property():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_batch_update_properties():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_put_edge():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_batch_put_edge():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_upsert_edge():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_batch_upsert_edge():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_drop_node():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_batch_drop_node():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_drop_edge():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_batch_drop_edge():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_get_node():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_list_node():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_get_edge():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200

    # def test_list_edge():
    #     query = "g.V().count()"

    #     result = nep.low_api(query)

    #     assert result["status_code"] == 200
