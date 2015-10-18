import serial
import time
import colour as c
import threading, queue
from LedEffects import LedEffects

__author__ = 'kurt'

header = b"Ada"
#header = "\x41\x64\x61"
NUM_LEDS = 80



leds_byte = ""
led = c.Color("blue")

leds_list =[]
for i in range(NUM_LEDS+1):
    leds_list.append(led)


blue = c.Color("blue")

'''serial setup'''
ser = serial.Serial("COM4",115200)

'''initialize class'''
LedEff = LedEffects(header,ser,NUM_LEDS)


LedEff.chase()
print("sleeping now")
time.sleep(10)
print("stopping now")
LedEff.stop()



#ser.write(leds_list_to_byte())

