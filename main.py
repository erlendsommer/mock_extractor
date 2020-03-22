import logging
from time import monotonic
from datetime import timedelta
# modules
from modules.cognite.cogniteAPI import CogniteService
from modules.sautervision.sautervisionAPI import *
from modules.goiot.goiotAPI import *


class DataExtractor:
    modules = dict(Sautervision=SauterVisionAPI,
                   GoIoT=GoiotAPI)

    def __init__(self, client_info):
        self.start_time = monotonic()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("Data Extractor")
        self.client_system, self.env_vars = client_info
        self.cognite_service = CogniteService()
        self.client_service = None
        self.cognite_assets = []
        self.data_points = []

    def login_cognite_client(self):
        self.cognite_service.login()

    def retrieve_assets(self):
        for sensor in self.cognite_service.retieve_assets_list():
            if self.client_system in sensor.get("source"):
                self.cognite_assets.append(sensor)

    def login_client_endpoint(self):
        cdf_client = self.modules[self.client_system](self)
        self.client_service = cdf_client.login()

    def extract_data(self):
        for sensor in self.cognite_assets:
            data_point = self.client_service.data_extract(sensor)
            if data_point:
                self.data_points.append(data_point)

    def upload(self):
        if self.data_points:
            self.cognite_service.upload_data_points(self.data_points)
        failed_uploads = (len(self.cognite_assets) - self.cognite_service.total_uploads)
        session_time = timedelta(seconds=monotonic() - self.start_time)
        self.logger.info(f"Session time:{str(session_time)} \n"
                         f"Total number of objects in list: {len(self.cognite_assets)} \n"
                         f"Total number of objects uploaded to CDF: {self.cognite_service.total_uploads} \n"
                         f"Objects with no data or with failure: {failed_uploads}")


def pipeline(system, env_vars):
    extractor = DataExtractor((system, env_vars))
    extractor.login_cognite_client()
    extractor.retrieve_assets()
    if not extractor.cognite_assets:
        extractor.logger.error("no assets in list")
    extractor.login_client_endpoint()
    extractor.extract_data()
    extractor.upload()


if __name__ == '__main__':
    # ARGS
    system = "Sautervision"
    env_vars = dict(passw="1234", username="user")
    pipeline(system, env_vars)
