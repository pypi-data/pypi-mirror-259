import logging
from vesselasid.asid import Asid


class VesselAsidRenderer:
    def __init__(self, asid):
        self.asid = asid

    def start(self):
        return

    def stop(self):
        return

    def note_on(self, msg):
        logging.debug(msg)

    def note_off(self, msg):
        logging.debug(msg)

    def control_change(self, msg):
        logging.debug(msg)

    def pitchwheel(self, msg):
        logging.debug(msg)
