import time

from influxdb import InfluxDBClient
import requests


class DataHandler:
    def __init__(self, opt):
        self.opt = opt
        self.offset = 0

        try:
            self.client = InfluxDBClient(host=opt["influx"]["host"], port=opt["influx"]["port"])
            dbs = self.client.get_list_database()

            if not {'name' : self.opt["influx"]["db_name"]} in dbs:
                self.client.create_database(self.opt["influx"]["db_name"])

            self.client.switch_database(self.opt["influx"]["db_name"])
            self.available = True

        except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout, ConnectionRefusedError) as err:
            self.available = False
            print(err)
            print("Connection to Influx DB failed")
            print("host=" + opt["influx"]["host"])
            print("port=" + str(opt["influx"]["port"]))


    def uploadDataInput(self, di):
        print("upload")
        #if self.offset == 0:
        #    self.offset = di.timestamp - int(time.time())

        #di.timestamp = di.timestamp - self.offset

        self.uploadDatapoints(di.asDatapoints())

    def uploadDatapoints(self, datapoints):
        self.client.write_points([dp.__dict__ for dp in datapoints], time_precision='s')