import logging


class ComputeStuffAPI:

    def __init__(self):
        self.logger = logging.getLogger("Compute")

    def login_details(self, env_vars):# TODO: denne må du forklare bedre
        return False

    def compute_this(self):
        erlend = "is smart"
        if erlend:
            return dict(timestamp=150000000000, value="The greatest man alive")

    def data_extract(self, sensor):
        response = self.compute_this()
        return dict(externalId=sensor.get("external_id"),
                    datapoints=[response])