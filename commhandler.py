import threading
import time
from datainput import *

@dataclass
class Request:
    command: str
    last_attempt: int = 0
    attempt: int = 0


class CommHandler(threading.Thread):
    def __init__(self, opt, sh, dh):
        super().__init__()

        self.opt = opt
        self.sh = sh #serial handler
        self.dh = dh #data handler
        #self.uih = uih #ui handler
        self.open_requests = {}
        self.request_id = 1

    def setUIHandler(self, uih):
        self.uih = uih

    def updateUI(self, last_rec, connected, arrow_state, info_state):
        pass


    def run(self):

        while True:

            if self.sh.input_available():  # handle inputs from solar car
                l = self.sh.get_next_input()

                di = DataInput()
                match l.split(":")[0]:
                    case "d":
                        di = CSVLine(self.opt, l)
                    case "c":
                        di = CANFrame(self.opt, l)
                    case "a":
                        req_id = int(l.split(":")[1].split(",")[0])
                        success = int(l.split(",")[1].strip()) == 1

                        if req_id in self.open_requests:
                            di = RequestAck(self.open_requests[req_id], success)
                            self.ackRequest(l)

                self.dh.uploadDataInput(di)

            for req_id in self.open_requests.keys():  # handler outgoing requests to solar car
                r = self.open_requests[req_id]
                if (int(time.time()) - r.last_attempt) >= self.opt["comm"]["retry_timeout"]:
                    self.sh.out_queue.append(r.command)
                    self.open_requests[req_id].attempt += 1
                    self.open_requests[req_id].last_attempt = int(time.time())

                    if self.open_requests[req_id].attempt >= self.opt["comm"]["req_attempts"]:
                        self.open_requests.pop(req_id)

            self.uih.updateRequestList()

    def ackRequest(self, input_str):
        req_number = int(input_str.split(":")[1].split(",")[0])
        success = input_str.split(":")[1].split(",")[1]

        self.open_requests.pop(req_number, None)

    def setSpeedArrow(self, direction, turn_off):
        #direction should be "u" for up or "d" for down
        cmd = "r:" + str(self.request_id) \
              + "," + direction \
              + ("-" if turn_off else "") + "\n"

        self.request_id += 1

        req = Request(cmd)
        self.open_requests.append(req)

    def setDriverInfo(self, warn, text):
        cmd = "r:" + str(self.request_id) \
              + (",!" if warn else ",:") \
              + text[:self.opt["comm"]["driver_info_length"]] \
              + "\n"

        self.request_id += 1

        req = Request(cmd)
        self.open_requests.append(req)