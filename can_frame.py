import struct


class CANFrame:
    def __init__(self, opt):
        self.opt = opt
        self.addr = 0
        self.data = 0

    def __int__(self, opt, serial_point):
        self.opt = opt
        self.addr = int(serial_point[1], 16)
        self.data = int(serial_point[2], 16)

    def get_data_i(self, length, signed, index):
        mask = 0
        signed_mask = 0x1 << length # Example: 0x100 for length = 8

        for i in range(length/4): # Example: 0xFF for length = 8
            mask = (mask << 1) | 0xF

        val = self.data >> (index * length) & mask

        if signed and val >= (0x8 << (length - 4)): # Example (0x8 << (length - 4)): 0x80 for length = 8
            val -= signed_mask

        return val

    def get_data_f(self, index):
        raw = self.data >> (index * 32) & 0x00000000FFFFFFFF

        s = struct.pack('>L', raw)
        return struct.unpack('>f', s)[0]
