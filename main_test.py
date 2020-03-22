import unittest
from main import main, SauterVisionAPI, GoiotAPI
from modules.cognite.cogniteAPI import CogniteAPI
from unittest.mock import MagicMock


class TestPipeline(unittest.TestCase):
    def test_sautervision(self):
        system = "Sautervision"
        env_vars = dict(passw="1234", username="user")
        client_service = SauterVisionAPI(env_vars)
        main(system, client_service, CogniteAPI())

        #assert called

    def test_goiot(self):
        system = "GoIoT"
        env_vars = dict(passw="1234", username="user")
        client_service = GoiotAPI(env_vars)
        main(system, client_service, CogniteAPI())

        #assert called
