import logging


class SauterVisionAPI:
    base_url = "/VisionCenterApiService/api"
    headers = {'Content-Type': "application/json", 'Cache-Control': "no-cache"}

    def __init__(self):
        self.logger = logging.getLogger("Sautervision")
        # self.login_response = None

    def login_details(self, env_vars):
        password = env_vars.get("passw")
        username = env_vars.get("username")
        payload = dict(Login=username, Password=password)
        url = f"http://{env_vars.get('ip')}{SauterVisionAPI.base_url}/Login"
        return dict(payload=payload, url=url)

    def client_request(self):
        # if self.login_response: #todo: hva skulle denne representere?
        return dict(timestamp=150000000000, value=20)

    def data_extract(self, sensor):
        response = self.client_request()
        return dict(externalId=sensor.get("external_id"),
                    datapoints=[response])
