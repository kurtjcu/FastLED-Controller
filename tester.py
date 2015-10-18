import serial
import time
import colour as c
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

ser = serial.Serial("COM4",115200)

LedEff = LedEffects(header,ser,NUM_LEDS)


LedEff.chase()

'''
while True:
	for i in range(NUM_LEDS):
		leds_list = [ c.Color("black") ] * NUM_LEDS
		leds_list[i] = c.Color(rgb=(1, 1, 1))
		ser.write(leds_list_to_byte())
		time.sleep(0.01)
'''

#ser.write(leds_list_to_byte())

