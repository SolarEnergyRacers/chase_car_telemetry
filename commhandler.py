import threading

class CommHandler(threading.Thread):
    def __init__(self, options):
        self.options = options

    def run(self):
        while(True):
            pass