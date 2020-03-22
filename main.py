import logging
import sys
from time import monotonic
from datetime import timedelta
# modules
from modules.cognite.cogniteAPI import CogniteAPI
from modules.sautervision.sautervisionAPI import *
from modules.goiot.goiotAPI import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Data Extractor")


def main(system, client_service, cognite_service):
    start_time = monotonic()
    cognite_service.login()
    assets = list(filter(lambda x: system in x.get("source"), cognite_service.retieve_assets_list()))
    failed_uploads = -1
    if assets:
        client_service.login()
        data_points = list(map(lambda x: client_service.data_extract(x), assets))
        cognite_service.upload_data_points(data_points)
        failed_uploads = (len(data_points) - cognite_service.total_uploads)
    session_time = timedelta(seconds=monotonic() - start_time)
    logger.info(f"Session time:{str(session_time)} \n"
                f"Total number of objects in list: {len(assets)} \n"
                f"Total number of objects uploaded to CDF: {cognite_service.total_uploads} \n"
                f"Objects with no data or with failure: {failed_uploads}")


if __name__ == '__main__':
    # ARGS

    if len(sys.argv) == 4:
        system = sys.argv[1]
        env_vars = dict(passw=sys.argv[2], username=sys.argv[3])
    else:
        system = "Sautervision"
        env_vars = dict(passw="1234", username="user")

    modules = dict(Sautervision=SauterVisionAPI(env_vars),
                   GoIoT=GoiotAPI(env_vars)
                   )
    client_service = modules[system]
    main(system, client_service, CogniteAPI())
