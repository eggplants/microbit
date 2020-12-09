from motor import Motor
from microbit import *
m = Motor(pin0, pin1, pin2)
while True:
  m.start_forward(speed=0)