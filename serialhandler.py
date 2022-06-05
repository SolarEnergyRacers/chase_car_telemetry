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

    def run(self):
        while True:
            try:
                if self.com_available and self.com.inWaiting() > 0:
                    input_val = self.com.read_until()  # reads until \n by default
                    self.in_queue.append(input_val)
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
            self.com = serial.Serial(self.options.com, self.options.baud)
            self.com_available = True
        except SerialException:
            print("Failed to open Serial Connection")
            self.com_available = False
