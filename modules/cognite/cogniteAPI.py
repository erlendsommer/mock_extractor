import logging


class CogniteService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.cognite_client = None
        self.total_uploads = 0

    def login(self):
        try:
            self.cognite_client = True
        except Exception as err:
            self.logger.error(err)
        else:
            self.logger.info("Successful login to Cognite")

    def upload_data_points(self, data):
        if self.cognite_client and data:
            self.logger.info(f"Upload complete, data= {data}")
            self.total_uploads += len(data)

    def retieve_assets_list(self):
        return [dict(external_id="Drammensveien_145_1", source="Sautervision",
                     metadata=dict(sensorId="RT001", TS_name="ONE")),
                dict(external_id="Drammensveien_145_2", source="Sautervision",
                     metadata=dict(sensorId="RT002", TS_name="TWO")),
                dict(external_id="Storgata_33_1", source="Sautervision",
                     metadata=dict(sensorId="RT001", TS_name="ONE")),
                dict(external_id="Storgata_33_2", source="Sautervision",
                     metadata=dict(sensorId="RT002", TS_name="TWO")),
                dict(external_id=3, source="GoIoT", metadata=dict(sensorId="JV001", TS_name="THREE")),
                dict(external_id=4, source="GoIoT", metadata=dict(sensorId="JV002", TS_name="FOUR")),
                dict(external_id=5, source="Compute", metadata=dict(sensorId="calc", TS_name="FIVE"))]

