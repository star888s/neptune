import pytest

# gremlin
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


# TODO endpointを環境変数に
class Fixtures:
    @pytest.fixture
    def __init__(self, endpoint) -> None:
        self.endpoint = endpoint

        self.traversal = traversal().withRemote(
            DriverRemoteConnection(endpoint, "g", verify_ssl=False)
        )
        pass

    @pytest.fixture
    def add_data(self):
        g = self.traversal
        g.addV("1234").property("name", "user01").next()
        yield
        g.V().hasLabel("1234").drop().iterate()
