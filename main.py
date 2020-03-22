import logging
import sys
from time import monotonic
from datetime import timedelta
# modules
from modules.cognite.cogniteAPI import CogniteAPI
from modules.compute.computeStuffAPI import ComputeStuffAPI
from modules.sautervision.sautervisionAPI import *
from modules.goiot.goiotAPI import *
from utils.login import Login

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Data Extractor")


def main(system, env_vars, client_service, cognite_service):
    start_time = monotonic()
    cognite_service.login()
    assets = list(filter(lambda x: system in x.get("source"), cognite_service.retieve_assets_list()))
    if assets:
        data_points = []
        for building in env_vars:
            Login(system, building, client_service)
            data_points.append(list(map(lambda x: client_service.data_extract(x), assets)))
        cognite_service.upload_data_points(data_points)
        failed_uploads = (len(data_points) - cognite_service.total_uploads)
    session_time = timedelta(seconds=monotonic() - start_time)
    logger.info(f"Session time:{str(session_time)} \n"
                f"Total number of objects in list: {len(assets)} \n"
                f"Total number of objects uploaded to CDF: {cognite_service.total_uploads} \n"
                f"Objects with no data or with failure: {failed_uploads}") #todo sjekk høyde for ingen data


if __name__ == '__main__':
    # ARGS
    system = "Sautervision"
    env_vars_Drammensveien = dict(passw="1234", username="user", ip="213.52.59.36")
    env_vars_Storgata = dict(passw="123434", username="user_34", ip="109.74.177.206:8080")
    env_vars = [env_vars_Drammensveien, env_vars_Storgata]
    modules = dict(Sautervision=SauterVisionAPI()
                   , GoIoT=GoiotAPI()
                   , Compute=ComputeStuffAPI()
                   )
    client_service = modules[system]
    main(system, env_vars, client_service, CogniteAPI())
