import json
from datahandler import DataHandler
from commhandler import CommHandler
from datapoint import DataPoint
from datainput import CANFrame
from serialhandler import SerialHandler
from serialsim import SerialSim

if __name__ == "__main__":

    with open("options.json", "r") as opt_file:
        opt = json.load(opt_file)
        print(opt)

    sh = SerialSim(opt)
    dh = DataHandler(opt)

    ch = CommHandler(opt, sh, dh)

    sh.start()
    ch.start()

    #dp = DataPoint("Temperature", {"car": "SER4"}, 1653216019, {"value": 45.6})
    #dh = DataHandler(opt)
    #dh.uploadDatapoints([dp])

    #c = CANFrame(opt, "c::1653830071,6A0,100")
    #print(c.timestamp)
    #print(c.addr)
    #print(c.data)
    #print(c.get_data_i(8, False, 1))

    # Start Serial receiver Thread
    #rec = SerialHandler(opt)
    #rec.start()