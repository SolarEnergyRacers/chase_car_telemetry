import json
import logging as lg
import sys

from PyQt5 import QtWidgets

from datahandler import DataHandler
from commhandler import CommHandler
from serialhandler import SerialHandler
from serialsim import SerialSim
from uihandler import UIHandler

if __name__ == "__main__":

    # read config file
    with open("options.json", "r") as opt_file:
        opt = json.load(opt_file)

    # set console logging level
    if opt["app"]["debug"]:
        lg.root.setLevel(lg.DEBUG)
    else:
        lg.root.setLevel(lg.INFO)

    # sh = SerialSim(opt)
    sh = SerialHandler(opt)
    dh = DataHandler(opt)

    # CommHandler can take any object that implements run, input_available, get_next_input and add_output in place of sh
    ch = CommHandler(opt, sh, dh)

    app = QtWidgets.QApplication(sys.argv)
    uih = UIHandler(ch)
    uih.show()

    ch.mutex.acquire()
    ch.setUIHandler(uih)
    ch.mutex.release()

    sh.start()
    ch.start()

    sys.exit(app.exec_())
