from microbit import *

class Motor(object):
    def __init__(self, pinvref: MicroBitTouchPin,
                 pin1: MicroBitTouchPin, pin2: MicroBitTouchPin):
        self.pinvref = pinvref
        self.pin1 = pin1
        self.pin2 = pin2
    def start_forward(self, speed=127, delay=1000):
        self.pinvref.write_analog(speed)
        self.pin1.write_digital(1)
        self.pin2.write_digital(0)
        sleep(delay)
    def start_backward(self, speed=127, delay=1000):
        self.pinvref.write_analog(speed)
        self.pin1.write_digital(0)
        self.pin2.write_digital(1)
        sleep(delay)
    def stop(self, delay=1000):
        self.pin1.write_digital(1)
        self.pin2.write_digital(1)
        sleep(delay)
    def brake(self, delay=1000):
        self.pin1.write_digital(1)
        self.pin2.write_digital(1)
        sleep(delay)
