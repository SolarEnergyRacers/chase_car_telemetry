import threading
from threading import Lock
import time
from datainput import *
from uihandler import UIHandler


@dataclass
class Request:
    id: int
    command: str
    last_attempt: int = 0
    attempt: int = 0
    done = False


class CommHandler(threading.Thread):
    def __init__(self, opt, sh, dh):
        super().__init__()

        self.opt = opt
        self.sh = sh #serial handler
        self.dh = dh #data handler
        #self.uih = uih #ui handler
        self.open_requests = {}
        self.request_id = 1
        self.uih = None

        self.last_received = "no data"
        self.speed_arrow = "no data"
        self.driver_info = "no data"

        self.mutex = Lock()

    def setUIHandler(self, uih: UIHandler):
        self.uih = uih

    def updateUI(self):
        if self.uih:
            self.uih.setLastReceivedTime(self.last_received)
            self.uih.setTelemetryAvailable(str(self.sh.com_available))
            self.uih.setSpeedArrowState(self.speed_arrow)
            self.uih.setDriverInfoState(self.driver_info)
            self.uih.updateRequestList(self.open_requests)


    def run(self):

        while True:
            self.mutex.acquire()

            if self.sh.input_available():  # handle inputs from solar car
                self.last_received = time.strftime("%H:%M:%S")

                l = self.sh.get_next_input()
                di = DataInput()

                match l.split(":")[0]:
                    case "d":
                        di = CSVLine(self.opt, l)

                        self.driver_info = l.split(",")[self.opt["data"].index({"csv_header": "driverInfo", "txt_header": "Driver Info", "type": "str"})]
                        self.speed_arrow = l.split(",")[self.opt["data"].index({"csv_header": "speedArrow", "txt_header": "Speed Arrow", "type": "str"})]

                    case "c":
                        di = CANFrame(self.opt, l)
                    case "a":
                        req_id = int(l.split(":")[1].split(",")[0])
                        success = int(l.split(",")[1].strip()) == 1

                        if req_id in self.open_requests:
                            di = RequestAck(self.open_requests[req_id], success)
                            self.ackRequest(l)

                self.dh.uploadDataInput(di)

            open_reqs = self.open_requests
            for req_id in open_reqs.keys():  # handle outgoing requests to solar car
                r = self.open_requests[req_id]
                if (int(time.time()) - r.last_attempt) >= self.opt["comm"]["retry_timeout"]:
                    self.sh.out_queue.append(r.command)
                    self.open_requests[req_id].attempt += 1
                    self.open_requests[req_id].last_attempt = int(time.time())

                    if self.open_requests[req_id].attempt >= self.opt["comm"]["req_attempts"]:
                        self.open_requests[req_id].done = True

            for req in self.uih.out_req:
                self.open_requests[req.id] = req


            # keep UI up to date
            self.uih.updateRequestList(self.open_requests)
            self.updateUI()

            self.mutex.release()
            time.sleep(0.5)

    def ackRequest(self, input_str):
        req_number = int(input_str.split(":")[1].split(",")[0])
        success = input_str.split(":")[1].split(",")[1]

        self.open_requests.pop(req_number, None)

    def setSpeedArrow(self, direction):
        #direction should be "u" for up, "d" for down and "o" for off
        cmd = "r:" + str(self.request_id) \
              + ",a" + direction + "\n"

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


    def getDriverInfoReq(self, warn, text):
        self.request_id += 1
        cmd = "r:" + str(self.request_id) \
              + (",!" if warn else ",:") \
              + text[:self.opt["comm"]["driver_info_length"]] \
              + "\n"

        return Request(self.request_id, cmd)
