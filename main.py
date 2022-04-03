import json
from serialhandler import SerialHandler

if __name__ == "__main__":

    with open("options.json", "r") as opt_file:
        opt = json.load(opt_file)
        print(opt)

    # Start Serial receiver Thread
    #rec = SerialHandler(opt)
    #rec.start()