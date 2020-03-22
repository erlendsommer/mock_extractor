import requests
from modules.sautervision.sautervisionAPI import *
from modules.goiot.goiotAPI import *
from modules.compute.computeStuffAPI import *
logger = logging.getLogger("utils login")


class Login:

    def __init__(self, system, building, client_service):
        self.system = system
        self.client_service = client_service
        self.login_details = self.client_service.login_details(building)
        if self.login_details:
            self.request_login()

    def request_login(self):
        r = "YOU SHALL NOT PASS!!!!!!!!"
        try:
            #session = requests.session()
            if self.login_details.get("secret_file"):
                if self.client_service.pem_file == "secret":
                    r = "YOU MAY ENTER FILTHY HUMAN"
                    url = self.login_details.get("url")
                # r = session.post(url=self.client_service.url,
                #                  data=self.client_service.payload,
                #                  headers=self.client_service.headers,
                #                  verify=self.client_service.pem_file)
            else:
                if self.login_details.get("payload") and self.login_details.get("url"):
                    r = "YOU MAY ENTER FILTHY HUMAN"
                    url = self.login_details.get("url")
            #     r = session.post(url=self.client_service.url,
            #                      data=self.client_service.payload,
            #                      headers=self.client_service.headers)
            #
            # if r.status_code != 200:
            #     logger.error(f"Login to {self.system} failed. Status code:{str(r.status_code)}, response: {r.text}")
            #     raise ConnectionError(f"Login to {self.system} failed")
        except ConnectionError as err:
            logger.error(f"Connection error {str(err)}")
        except TimeoutError as err:
            logger.error(f"Timeout error {str(err)}")
        except Exception as err:
            logger.error(str(err))
        else:
            logger.info(f"Successful login to {self.system} with this url: {url}")
            #self.client_service.login_response = r todo: hva skal dette være i virkeligheten
            return self.client_service
