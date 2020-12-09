from motor import Motor
from microbit import *

m=Motor(pin0, pin1, pin2)

def count_10times():
    for _ in range(10):
           display.show(_)
           sleep(1000)


while True:
   if button_a.is_pressed():
       m.start_forward(speed=500)
       count_10times()
       m.stop()
   if button_b.is_pressed():
       m.start_backward(speed=500)
       count_10times()
       m.stop()
