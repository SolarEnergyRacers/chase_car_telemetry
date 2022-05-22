#Use as abstract class
class DataInput:
    def __init__(self):
        self.timestamp = 0
        pass

    def asDatapoints(self):
        raise NotImplementedError("Please Implement this method")
