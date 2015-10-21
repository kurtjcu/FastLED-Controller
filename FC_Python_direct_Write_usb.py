import serial
import random
import time
import binascii

__author__ = 'kurt'

#!/usr/bin/env python
#
# Basic example for Fadecandy, talking directly to the
# Teensy using PyUSB.
#
# Micah Elizabeth Scott
# This example code is released into the public domain.
#

ser = serial.Serial("COM4",115200)

'''
dev = serial.Serial("COM4",115200)
if not dev:
    raise IOError("No Fadecandy interfaces found")
'''

#dev.set_configuration()

print("Serial number: {}".format("Herro"))

# Debug flags

flags = 0x00
#dev.write('\x80' + chr(flags) + ('\x00' * 62))

# Set up a default color LUT
'''
lut = [0] * (64 * 25)
for index in range(25):
    lut[index*64] = index | 0x40
lut[24*64] |= 0x20
for channel in range(3):
    for row in range(257):
        value = min(0xFFFF, int(pow(row / 256.0, 2.2) * 0x10000))
        i = channel * 257 + row
        packetNum = i / 31
        packetIndex = i % 31
        print("%d, %d = 0x%04x" % (channel, row, value))
        lut[int(packetNum*64 + 2 + packetIndex*2)] = value & 0xFF
        lut[int(packetNum*64 + 3 + packetIndex*2)] = value >> 8
lutPackets = ''.join(map(chr, lut))
print(binascii.b2a_hex(lutPackets.encode()))
#dev.write(1, lutPackets)
print("LUT programmed")
'''

# Slowly push random frames to the device

print("beer now")
while True:

    for index in range(25):
        if index == 24:
            # Final
            control = index | 0x20
        else:
            control = index

        data = bytes([control])

        for i in range(4):
            print('----herro----')
            data += bytes([random.choice([0, 255])])

        print (len(data))
        print(binascii.b2a_hex(data))
        ser.write(data)

        print(ser.readline())
        #out = ""
        #while ser.inWaiting() > 0:
        #    print(ser.read())



    print('ended')
    #raw_input()
    #time.sleep(0.1)

