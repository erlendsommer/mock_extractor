import logging
from time import monotonic
from datetime import timedelta
# modules
from modules.cognite.cogniteAPI import CogniteAPI
from modules.sautervision.sautervisionAPI import *
from modules.goiot.goiotAPI import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Data Extractor")


def get_api_implementation(system, env_vars):
    if system == "Sautervision":
        return SauterVisionAPI(env_vars)
    elif system == "GoIoT":
        return GoiotAPI(env_vars)
    else:
        raise Exception("mangler system")


def retrieve_assets(cognite_service, client_system):
    cognite_assets = []
    for sensor in cognite_service.retieve_assets_list():
        if client_system in sensor.get("source"):
            cognite_assets.append(sensor)
    return cognite_assets



def extract_data(assets, client_service):
    data_points = []
    for sensor in assets:
        data_point = client_service.data_extract(sensor)
        if data_point:
            data_points.append(data_point)
    return data_points


if __name__ == '__main__':
    # ARGS
    start_time = monotonic()
    system = "Sautervision"
    env_vars = dict(passw="1234", username="user")
    client_service = get_api_implementation(system, env_vars)
    cognite_service = CogniteAPI()
    cognite_service.login()
    assets = retrieve_assets(cognite_service, system)
    if assets:
        client_service.login()
        data_points = extract_data(assets, client_service)
        cognite_service.upload_data_points(data_points)
        session_time = timedelta(seconds=monotonic() - start_time)
        failed_uploads = (len(data_points) - cognite_service.total_uploads)
        logger.info(f"Session time:{str(session_time)} \n"
                    f"Total number of objects in list: {len(assets)} \n"
                    f"Total number of objects uploaded to CDF: {cognite_service.total_uploads} \n"
                    f"Objects with no data or with failure: {failed_uploads}")
