import unittest
from main import main, SauterVisionAPI, GoiotAPI
from modules.cognite.cogniteAPI import CogniteAPI
from unittest.mock import MagicMock

from modules.compute.computeStuffAPI import ComputeStuffAPI


# TODO: lær MagicMock

class TestPipeline(unittest.TestCase):
    def test_sautervision(self):
        system = "Sautervision"
        env_vars_Drammensveien = dict(passw="1234", username="user", ip="213.52.59.36")
        env_vars_Storgata = dict(passw="123434", username="user_34", ip="109.74.177.206:8080")
        env_vars = [env_vars_Drammensveien, env_vars_Storgata]

        client_service = SauterVisionAPI()
        main(system, env_vars, client_service, CogniteAPI())

        # assert called

    def test_goiot(self):
        system = "GoIoT"
        env_vars_Drammensveien = dict(passw="1234", username="user", ip="213.52.59.36")
        env_vars_Storgata = dict(passw="123434", username="user_34", ip="109.74.177.206:8080")
        env_vars = [env_vars_Drammensveien, env_vars_Storgata]

        client_service = GoiotAPI()
        main(system, env_vars, client_service, CogniteAPI())

        # assert called

    def test_Compute(self):
        system = "Compute"
        env_vars_Drammensveien = dict(passw="1234", username="user", ip="213.52.59.36")
        env_vars_Storgata = dict(passw="123434", username="user_34", ip="109.74.177.206:8080")
        env_vars = [env_vars_Drammensveien, env_vars_Storgata]

        client_service = ComputeStuffAPI()
        main(system, env_vars, client_service, CogniteAPI())

        # assert called
