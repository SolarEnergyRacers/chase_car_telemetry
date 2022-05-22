import math
import struct
from datapoint import DataPoint
from datainput import DataInput


class CANFrame(DataInput):
    def __init__(self, opt):
        DataInput.__init__(self)
        self.opt = opt
        self.timestamp = 0
        self.addr = 0
        self.data = 0

    def __int__(self, opt, serial_str):
        self.opt = opt
        self.timestamp = int(serial_str.split(",")[0][3:], 10)
        self.addr = int(serial_str.split(",")[1], 16)
        self.data = int(serial_str.split(",")[2], 16)

    def get_data_i(self, length, signed, index):
        mask = 0
        signed_mask = 0x1 << length  # Example: 0x100 for length = 8

        for i in range(length / 4):  # Example: 0xFF for length = 8
            mask = (mask << 1) | 0xF

        val = self.data >> (index * length) & mask

        if signed and val >= (0x8 << (length - 4)):  # Example (0x8 << (length - 4)): 0x80 for length = 8
            val -= signed_mask

        return val

    def get_data_b(self, index):
        return self.get_data_i(1, False, index) == 1

    def get_data_f(self, index):
        raw = self.data >> (index * 32) & 0x00000000FFFFFFFF

        s = struct.pack('>L', raw)
        return struct.unpack('>f', s)[0]

    def isBMSFrame(self):
        return int(self.opt["CAN"]["MPPT"]["base_addr"], 16) == (self.addr & 0xF00)

    def isMPPTFrame(self):
        return int(self.opt["CAN"]["MPPT"]["base_addr"], 16) == (self.addr & 0xF00)

    def asDatapoints(self):
        datapoints = []
        mppt_baseaddr = int(self.opt["CAN"]["MPPT"]["base_addr"], 16)
        bms_baseaddr = int(self.opt["CAN"]["BMS"]["base_addr"], 16)

        # BMS
        if self.isBMSFrame():
            if self.addr == bms_baseaddr:  # BMU Heartbeat/Serialnumber
                datapoints.append(DataPoint("bms_heartbeat",
                                            {"bmu_id": self.get_data_i(32, False, 1)},
                                            self.timestamp,
                                            {"value": True}))

            elif self.addr & 0xFF <= 0xEF:  # CMU Status, cell data
                cmu_num = math.floor(((self.addr & 0xFF)-1) / 3)  # CMU0 = 0x601, 0x602, 0x603 CMU1 = 0x604, 0x605 etc..

                if self.addr & 0xFF in [0x01, 0x04, 0x07, 0x0A]:  # CMU Serial Number & Temperatures
                    heartbeat = DataPoint("cmu_heartbeat", {"cmu_id": self.get_data_i(32, False, 0),
                                                            "cmu_num": cmu_num},
                                          self.timestamp, {"value": True})

                    pt = DataPoint("pcb_temp", {"cmu_num": cmu_num}, self.timestamp, {"value": self.get_data_i(16, True, 2) / 10})
                    ct = DataPoint("cell_temp", {"cmu_num": cmu_num}, self.timestamp, {"value": self.get_data_i(16, True, 3) / 10})

                    datapoints.append([heartbeat, pt, ct])

                elif self.addr & 0xFF in [0x02, 0x05, 0x08, 0x0B, 0x03, 0x06, 0x09, 0x0C]:  # Voltages 1 & 2
                    index_offset = 0
                    if (self.addr & 0xFF) % 3 == 0:
                        index_offset = 4

                    for i in range(4):
                        cell_volt = DataPoint("cell_voltage", {"cmu_num": cmu_num,
                                                               "cell_num": i + index_offset,
                                                               "cell_index": cmu_num * 8 + i + index_offset},
                                              self.timestamp, {"value": self.get_data_i(16, True, i)})
                        datapoints.append(cell_volt)

            elif self.addr & 0xFF == 0xF4:  # Pack SOC
                datapoints.append(DataPoint("soc_ah", {}, self.timestamp, {"value": self.get_data_f(0)}))
                datapoints.append(DataPoint("soc_perc", {}, self.timestamp, {"value": self.get_data_f(1)}))

            elif self.addr & 0xFF == 0xF5:  # Balance SOC
                datapoints.append(DataPoint("balance_ah", {}, self.timestamp, {"value": self.get_data_f(0)}))
                datapoints.append(DataPoint("balance_perc", {}, self.timestamp, {"value": self.get_data_f(1)}))

            elif self.addr & 0xFF == 0xF6:  # Charger Control Info
                # prob not relevant
                pass
            elif self.addr & 0xFF == 0xF7:  # Precharge Status
                # contactors
                datapoints.append(DataPoint("err_cont_1_driver", {}, self.timestamp, {"value": self.get_data_b(0)}))
                datapoints.append(DataPoint("err_cont_2_driver", {}, self.timestamp, {"value": self.get_data_b(1)}))
                datapoints.append(DataPoint("output_cont_1_driver", {}, self.timestamp, {"value": self.get_data_b(3)}))
                datapoints.append(DataPoint("output_cont_2_driver", {}, self.timestamp, {"value": self.get_data_b(4)}))
                datapoints.append(DataPoint("err_cont_12v_supply", {}, self.timestamp, {"value": not self.get_data_b(5)}))
                datapoints.append(DataPoint("err_cont_3_driver", {}, self.timestamp, {"value": self.get_data_b(6)}))
                datapoints.append(DataPoint("output_cont_3_driver", {}, self.timestamp, {"value": self.get_data_b(7)}))

                # precharge state
                precharge_state = ""
                match self.get_data_i(8, False, 1):
                    case 0:
                        precharge_state = "error"
                    case 1:
                        precharge_state = "idle"
                    case 2:
                        precharge_state = "measure"
                    case 3:
                        precharge_state = "precharge"
                    case 4:
                        precharge_state = "run"
                    case 5:
                        precharge_state = "enable"

                datapoints.append(DataPoint("prec_state", {}, self.timestamp, {"value": precharge_state}))

                # contactor supply voltage
                datapoints.append(DataPoint("cont_voltage", {}, self.timestamp, {"value": self.get_data_i(16, False, 1) / 1000}))

                datapoints.append(DataPoint("prec_timer_elapsed", {}, self.timestamp, {"value": self.get_data_b(6*8)}))
                datapoints.append(DataPoint("prec_timer", {}, self.timestamp, {"value": self.get_data_i(8, False, 7)}))

            elif self.addr & 0xFF == 0xF8:  # min/max cell voltage
                # redundant
                pass
            elif self.addr & 0xFF == 0xF9:  # min/max cell temp
                pass
            elif self.addr & 0xFF == 0xFA:  # Pack Voltage & Current
                pass
            elif self.addr & 0xFF == 0xFB:  # Pack Status
                pass
            elif self.addr & 0xFF == 0xFC:  # Fan & 12V Status
                pass
            elif self.addr & 0xFF == 0xFD:  # Ext. Pack Status
                pass
        # MPPT
        elif self.isMPPTFrame():  # handled separately
            if self.addr & 0xF == 0x0:  # MPPT input
                pass
            elif self.addr & 0xF == 0x1:  # MPPT output
                pass
            elif self.addr & 0xF == 0x2:  # Temps
                pass
            elif self.addr & 0xF == 0x3:  # Aux Power voltages
                pass
            elif self.addr & 0xF == 0x4:  # Limits
                pass
            elif self.addr & 0xF == 0x5:  # Status
                pass
            elif self.addr & 0xF == 0x6:  # Power Connector
                pass
        else:  # Prob. transmission error or wrong addresses configured
            pass

        return datapoints
