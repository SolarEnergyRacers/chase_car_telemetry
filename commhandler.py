import threading
from threading import Lock
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
        self.sh = sh  # serial handler
        self.dh = dh  # data handler
        # self.uih = uih #ui handler
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

                self.dh.uploadDataInput(di)

            for comm in self.uih.out_req:
                self.sh.out_queue.append(comm)

            self.uih.out_req.clear()

            # keep UI up to date
            #self.uih.updateRequestList(self.open_requests)
            self.updateUI()

            self.mutex.release()
            time.sleep(0.2)

    def ackRequest(self, input_str):
        req_number = int(input_str.split(":")[1].split(",")[0])
        success = input_str.split(":")[1].split(",")[1]

        self.open_requests.pop(req_number, None)

    def setSpeedArrow(self, direction):
        # direction should be "u" for up, "d" for down and "o" for off
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
