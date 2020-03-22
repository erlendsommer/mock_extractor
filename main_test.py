import unittest
from main import pipeline
from main import DataExtractor, SauterVisionAPI, GoiotAPI
from unittest.mock import MagicMock


class TestPipeline(unittest.TestCase):
    def test_sautervision(self):
        system = "Sautervision"
        env_vars = dict(passw="1234", username="user")
        login_class = SauterVisionAPI(env_vars)
        extractor = DataExtractor((system, login_class, env_vars))
        pipeline(extractor)

        self.assertEqual(2, len(extractor.cognite_assets))
        self.assertEqual(2, extractor.cognite_service.total_uploads)

    def test_goiot(self):
        system = "GoIoT"
        env_vars = dict(passw="1234", username="user")
        login_class = GoiotAPI(env_vars)
        extractor = DataExtractor((system, login_class, env_vars))
        pipeline(extractor)

        self.assertEqual(2, len(extractor.cognite_assets))
        self.assertEqual(2, extractor.cognite_service.total_uploads)
