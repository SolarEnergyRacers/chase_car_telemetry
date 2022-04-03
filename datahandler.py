import threading

from can_frame import CANFrame


class DataHandler(threading.Thread):
    def __init__(self, options):
        self.options = options

    def parseDataset(self, str):
        pass

    def parseCANFrame(self, str):
        frame = CANFrame(str);

    def uploadDatapoints(self, datapoints):
        pass