import time
import colour as c
import threading

__author__ = 'kurt'



class  LedEffects:

    def __init__(self,header,ser,NUM_LEDS):
        self.header = header
        self.ser = ser
        self.NUM_LEDS = NUM_LEDS

###################
#
#           Utilities v
#
###################

    def leds_list_to_byte(self,leds_list):
        temp_string = self.header
        for each in leds_list:
            for colour in each.get_rgb():
                temp_string += bytes([int(255 * colour)])
        return temp_string


###################
#
#           Effects
#
###################



    def chase(self, colour = c.Color(rgb=(1, 1, 1))):
        while True:
            for i in range(self.NUM_LEDS):
                leds_list = [ c.Color("black") ] * self.NUM_LEDS
                leds_list[i] = c.Color(rgb=(1, 1, 1))
                self.ser.write(self.leds_list_to_byte(leds_list))
                time.sleep(0.01)

