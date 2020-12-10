from microbit import *
from machine import time_pulse_us

def sonic(in1, in2):
    in1.write_digital(0)
    in2.read_digital()
    while True:
        in1.write_digital(1)
        in1.write_digital(0)
        time = time_pulse_us(in2, 1) / 10 ** 6
        dist = int(time / 2 * 34300)
        display.show(dist)
        sleep(100)

sonic(pin2, pin16)