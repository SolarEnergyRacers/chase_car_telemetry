import struct


class CANFrame:
    def __init__(self, opt):
        self.opt = opt
        self.timestamp = 0
        self.addr = 0
        self.data = 0

    def __int__(self, opt, str):
        self.opt = opt
        self.timestamp = int(str.split(",")[0][3:], 10)
        self.addr = int(str.split(",")[1], 16)
        self.data = int(str.split(",")[2], 16)

    def get_data_i(self, length, signed, index):
        mask = 0
        signed_mask = 0x1 << length  # Example: 0x100 for length = 8

        for i in range(length / 4):  # Example: 0xFF for length = 8
            mask = (mask << 1) | 0xF

        val = self.data >> (index * length) & mask

        if signed and val >= (0x8 << (length - 4)):  # Example (0x8 << (length - 4)): 0x80 for length = 8
            val -= signed_mask

        return val

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
                pass
            elif self.addr & 0xFF <= 0xEF:  # CMU Status, cell data
                pass
            elif self.addr & 0xFF == 0xF4:  # Pack SOC
                pass
            elif self.addr & 0xFF == 0xF5:  # Balance SOC
                pass
            elif self.addr & 0xFF == 0xF6:  # Charger Control Info
                pass
            elif self.addr & 0xFF == 0xF7:  # Precharge Stat    us
                pass
            elif self.addr & 0xFF == 0xF8:  # min/max cell voltage
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
