import serial
import time
import colour as c
import threading, queue
from LedEffects import LedEffects

__author__ = 'kurt'

header = b"Ada"
NUM_LEDS = 80



leds_byte = ""
led = c.Color("blue")
leds_list =[]
for i in range(NUM_LEDS+1):
    leds_list.append(led)


'''serial setup'''
ser = serial.Serial("COM4",115200)

'''initialize class'''
LedEff = LedEffects(header,ser,NUM_LEDS)

def main(args):

    # Create a single input and a single output queue for all threads.
    effect_q = queue.Queue()
    output_q = queue.Queue()

    # Create the "thread pool"
    effect = [LedEffects(header = header, effect_q=effect_q, output_q=output_q, NUM_LEDS = NUM_LEDS, ) for i in range(1)]

    # Start effect threads
    for thread in effect:
        thread.start()

    # Start Writer threads
    for thread in effect:
        thread.start()

    while output_q != "Finished":
        ser.write(output_q.get)

    print("sleeping now")
    time.sleep(10)
    print("stopping now")
    LedEff.stop()



#ser.write(leds_list_to_byte())

