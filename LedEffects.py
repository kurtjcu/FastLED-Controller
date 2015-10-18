import time
import colour as c
import threading, queue

__author__ = 'kurt'



class  LedEffects(threading.Thread):

    def __init__(self,header,ser,NUM_LEDS):
        super(LedEffects, self).__init__()
        self._stop = threading.Event()
        self.header = header
        self.ser = ser
        self.NUM_LEDS = NUM_LEDS

    """
    Use this to stop thread
    """
    def stop(self):
        self._stop.set()

    def join(self, timeout=None):
        self._stop.set()
        super(LedEffects, self).join(timeout)

    """
    Use this to see if thread has stopped
    """
    def stopped(self):
        return self._stop.isSet()


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



    def chase(self, colour = c.Color(rgb=(1, 1, 1))):
        while not self._stop.isSet():
            for i in range(self.NUM_LEDS):
                leds_list = [ c.Color("black") ] * self.NUM_LEDS
                leds_list[i] = c.Color(rgb=(1, 1, 1))
                self.ser.write(self.leds_list_to_byte(leds_list))
                time.sleep(0.01)


