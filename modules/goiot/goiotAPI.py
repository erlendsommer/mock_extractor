import logging


class GoiotAPI:
    ip = "82.221.35.197"
    headers = {'cache-control': "no-cache", "Content-Type": "application/json"}

    def __init__(self, extractor):
        self.extractor = extractor
        self.logger = logging.getLogger("GoIoT")
        self.password = extractor.env_vars.get("passw")
        self.username = extractor.env_vars.get("username")
        self.pem_file = "secret"
        self.payload = f"grant_type=password&username={self.username}&password={self.password}"
        self.url = f"https://{self.ip}/bacnetws/.auth/int/token"
        self.login_response = None

    def login_details(self):
        pem_file = "secret"
        payload = f"grant_type=password&username={self.username}&password={self.password}"
        url = f"https://{self.ip}/bacnetws/.auth/int/token"
        return dict(secret_file=pem_file, payload=payload, url=url)


    def client_request(self):
        if self.password and self.username:
            return dict(timestamp=150000000000, value=20)

    def data_extract(self, sensor):
        response = self.client_request()
        return dict(externalId=sensor.get("external_id"),
                    datapoints=[response])
