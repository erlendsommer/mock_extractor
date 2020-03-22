import logging
from time import monotonic
from datetime import timedelta
# modules
from modules.cognite.cogniteAPI import CogniteAPI
from modules.sautervision.sautervisionAPI import *
from modules.goiot.goiotAPI import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Data Extractor")


def get_client_api_implementation(system, env_vars):
    if system == "Sautervision":
        return SauterVisionAPI(env_vars)
    elif system == "GoIoT":
        return GoiotAPI(env_vars)
    else:
        raise Exception("mangler system")


if __name__ == '__main__':
    # ARGS
    start_time = monotonic()
    system = "Sautervision"
    env_vars = dict(passw="1234", username="user")
    cognite_service = CogniteAPI()
    cognite_service.login()
    assets = list(filter(lambda x: system in x.get("source"), cognite_service.retieve_assets_list()))
    failed_uploads = -1
    if assets:
        client_service = get_client_api_implementation(system, env_vars)
        client_service.login()
        data_points = list(map(lambda x: client_service.data_extract(x), assets))
        cognite_service.upload_data_points(data_points)
        failed_uploads = (len(data_points) - cognite_service.total_uploads)
    session_time = timedelta(seconds=monotonic() - start_time)
    logger.info(f"Session time:{str(session_time)} \n"
                f"Total number of objects in list: {len(assets)} \n"
                f"Total number of objects uploaded to CDF: {cognite_service.total_uploads} \n"
                f"Objects with no data or with failure: {failed_uploads}")