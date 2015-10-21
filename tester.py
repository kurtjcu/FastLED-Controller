import serial
import time
import colour as c
import threading, queue
from LedEffects import LedEffects

__author__ = 'kurt'

header = b"White"
#header = "\x41\x64\x61"
NUM_LEDS = 220



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


LedEff.chase(10, colour=c.Color("red"), offcolour=c.Color("blue"))




#ser.write(leds_list_to_byte())

