import time
import colour as c
import threading, queue

__author__ = 'kurt'



class  LedEffects():

    def __init__(self,header,ser,NUM_LEDS):
        self.header = header
        self.ser = ser
        self.NUM_LEDS = NUM_LEDS




###################
#
#           Utilities
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



    def chase(self,run_time, colour = c.Color(rgb=(1, 1, 1)), offcolour =c.Color("black")):

        t_end = time.time() + run_time
        while time.time() < t_end:
            for i in range(self.NUM_LEDS):
                leds_list = [ offcolour ] * self.NUM_LEDS
                leds_list[i] = colour
                self.ser.write(self.leds_list_to_byte(leds_list))
                time.sleep(0.01)


