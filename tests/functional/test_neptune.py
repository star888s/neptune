import pytest

# module
from main.neptune import Neptune

# gremlin
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


class TestNeptuneAccess:
    def test_low_api(add_data):
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_put_node():
        result = Neptune.put_node(item="1", properties={"name": "hoge", "name": "foo"})

        assert result["statusCode"] == 200

    def test_batch_put_node():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_upsert_node():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_update_property():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_batch_update_properties():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_put_edge():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_batch_put_edge():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_upsert_edge():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_batch_upsert_edge():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_drop_node():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_batch_drop_node():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_drop_edge():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_batch_drop_edge():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_get_node():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_list_node():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_get_edge():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200

    def test_list_edge():
        query = "g.V().count()"

        result = Neptune.low_api(query)

        assert result["statusCode"] == 200
