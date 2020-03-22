import unittest
from unittest.mock import MagicMock
from modules.cognite.cogniteAPI import CogniteAPI


class TestCogniteAPI(unittest.TestCase):
    def test_login(self):
        api = CogniteAPI()
        self.assertTrue(api.login())

    def test_retieve_assets_list(self):
        api = CogniteAPI()
        self.assertIsNotNone(api.retieve_assets_list())

    def test_upload_data_points(self):
        api = CogniteAPI()
        api.login()
        uploads = api.upload_data_points(
            dict({'externalId': 1, 'datapoints': [{'timestamp': 150000000000, 'value': 20}]}))
        self.assertEqual(uploads, 2)
