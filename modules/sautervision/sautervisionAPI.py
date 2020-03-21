import logging


class SauterVisionAPI:
    def __init__(self, extractor):
        self.extractor = extractor
        self.logger = logging.getLogger("Sautervision")
        self.password = extractor.env_vars.get("passw")
        self.username = extractor.env_vars.get("username")

    def login(self):
        if self.password and self.username:
            self.logger.info("Successful login to Sautervision")
            return self

    def client_request(self):
        if self.password and self.username:
            return dict(timestamp=150000000000, value=20)

    def data_extract(self, sensor):
        response = self.client_request()
        return dict(externalId=sensor.get("external_id"),
                    datapoints=[response])
