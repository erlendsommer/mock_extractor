import logging


class GoiotAPI:
    ip = "82.221.35.197"
    headers = {'cache-control': "no-cache", "Content-Type": "application/json"}

    def __init__(self):
        self.logger = logging.getLogger("GoIoT")
        self.pem_file = "secret"
       # self.login_response = None

    def login_details(self, env_vars):
        pem_file = "secret"
        payload = f"grant_type=password&username={env_vars.get('username')}&password={env_vars.get('password')}"
        url = f"https://{env_vars.get('ip')}/bacnetws/.auth/int/token"
        return dict(secret_file=pem_file, payload=payload, url=url)


    def client_request(self):
        #if self.password and self.username: todo: samme som sauter
        return dict(timestamp=150000000000, value=20)

    def data_extract(self, sensor):
        response = self.client_request()
        return dict(externalId=sensor.get("external_id"),
                    datapoints=[response])
