import threading
from datainput import *

class CommHandler(threading.Thread):
    def __init__(self, opt, sh, dh):
        super().__init__()

        self.opt = opt
        self.sh = sh #serial handler
        self.dh = dh #data handler
        self.open_requests = {}

    def run(self):

        while(True):

            if self.sh.input_available():
                l = self.sh.get_next_input()

                di = DataInput()
                match l.split(":")[0]:
                    case "d":
                        di = CSVLine(self.opt, l)
                    case "c":
                        di = CANFrame(self.opt, l)
                    case "a":
                        self.ackRequest(l)

                self.dh.uploadDataInput(di)

    def ackRequest(self, input_str):
        req_number = int(input_str.split(":")[1].split(",")[0])
        success = input_str.split(":")[1].split(",")[1]

        self.open_requests.pop(req_number, None)
