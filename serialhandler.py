import serial
from serial import SerialException

import threading
import time


class SerialHandler(threading.Thread):
    def __init__(self, options):
        super().__init__()

        self.options = options

        self.com = None
        self.com_available = False
        self.connect_serial()

        self.in_queue = []  # data being received from solar car
        self.out_queue = []  # data that will be sent to solar car

        self.last_beacon = 0.0

    def run(self):
        while True:
            try:
                if self.com_available:
                    if self.com.inWaiting() > 0:
                        input_val = self.com.read_until().decode()  # reads until \n by default


                        if input_val[:2] == "d:":
                            self.in_queue.append(input_val)
                            print(input_val)
                        else:
                            print("i:" + input_val)

                    if len(self.out_queue) > 0:
                        output_val = self.out_queue.pop()
                        self.com.write(output_val.encode("ascii", "ignore"))
                        print("o:" + output_val)

                    time.sleep(0.2)

                    #if time.time() - self.last_beacon > 0.75:
                    #    self.com.write("v\n".encode("ascii", "ignore"))
                    #    self.last_beacon = time.time()

                elif not self.com_available:
                    self.connect_serial()
                    time.sleep(0.5)

            except serial.SerialException:
                self.com.close()
                self.com_available = False
                print("SerialException")
            except TypeError:
                self.com.close()
                self.com_available = False
                print("TypeError")

    def input_available(self):
        return len(self.in_queue) > 0

    def get_next_input(self):
        if self.input_available():
            return self.in_queue.pop()
        else:
            return None

    def add_output(self, out_message):
        self.out_queue.append(out_message)

    def connect_serial(self):
        try:
            self.com = serial.Serial(self.options["serial"]["com"], self.options["serial"]["baud"])
            self.com_available = True
        except SerialException:
            print("Failed to open Serial Connection")
            self.com_available = False
