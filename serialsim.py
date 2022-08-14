import threading
import time
import random


class SerialSim(threading.Thread):
    def __init__(self, options):
        super().__init__()

        self.options = options

        self.com = None
        self.com_available = False
        self.connect_serial()

        self.in_queue = []  # data being received from solar car
        self.out_queue = []  # data that will be sent to solar car
        self.upt = 0



    def run(self):
        prev_data = {}

        while True:
            self.in_queue.append(self.get_rndm())
            time.sleep(1)

    def input_available(self):
        return len(self.in_queue) > 0

    def get_rndm(self):
        s = "d:"
        s += str(int(time.time())) + ","
        s += str(++self.upt) + ","
        s += "message,"
        s += str(random.random() * 100) + "," #speed
        s += str(random.randint(0, 255)) + "," #accelinp
        s += str(random.randint(0, 255)) + "," #decelinp
        s += str(random.randint(0, 255)) + "," #acceldisp
        s += str(random.choice(["true", "false"])) + ","
        s += str(round(random.random() * 80 + 20,3)) + "," #battvolt
        s += str(round(random.random() * 50,3)) + "," #battcurr
        s += "Battery Errors" + ","
        s += "Precharge State" + ","
        s += str(random.choice(["true", "false"])) + ","
        s += str(round(random.random() * 15,3)) + ","
        s += str(random.choice(["true", "false"])) + "," #motoron
        s += str(round(random.random() * 50,3)) + "," #motorcurr
        s += str(round(random.random() * 50,3)) + ","  # mppt1
        s += str(round(random.random() * 50,3)) + ","  # mppt2
        s += str(round(random.random() * 50,3)) + ","  # mppt3
        s += str(round(random.random() * 4.2,3)) + ","  # U cell min
        s += str(round(random.random() * 4.2,3)) + ","  # U cell avg
        s += str(round(random.random() * 4.2,3)) + ","  # U cell max
        s += str(round(random.random() * 30 + 20,3)) + ","
        s += str(round(random.random() * 30 + 20,3)) + ","
        s += str(round(random.random() * 30 + 20,3)) + ","
        s += str(round(random.random() * 30 + 20,3)) + ","
        s += str(random.choice(["OFF", "LEFT", "RIGHT", "HAZARD FLASHR"])) + ","
        s += str(random.choice(["fwd", "bwd"])) + ","
        s += str(random.choice(["true", "false"])) + ","
        s += str(random.choice(["true", "false"])) + ","
        s += "SomeString" + ","
        s += str(random.choice(["NONE", "SPEED", "POWER"])) + ","
        s += str(random.randint(0, 120)) + ","
        s += str(random.randint(0, 5000)) + ","
        s += "full send!" + ","
        s += str(random.choice(["OFF", "INCREASE", "DECREASE"])) + ","
        s += str(random.choice(["OFF", "L1", "L2"])) + ","
        s += "IOString" + "\n"
        return s

    def get_next_input(self):
        if self.input_available():
            return self.in_queue.pop()
        else:
            return None

    def add_output(self, out_message):
        pass

    def connect_serial(self):
        self.com_available = True
