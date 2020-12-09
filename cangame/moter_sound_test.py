from motor import Motor
from microbit import *
import music

m=Motor(pin0, pin1, pin2)

def count_10times():
    for _ in range(5):
           display.show(_)
           sleep(1000)

def play_beep():
    music.play(music.BA_DING, pin=pin8)

display.scroll("waiting...", wait=False)
while True:
   if button_a.is_pressed():
       m.start_forward(speed=500)
       count_10times()
       m.stop()
       play_beep()
       display.clear()
   if button_b.is_pressed():
       m.start_backward(speed=500)
       count_10times()
       m.stop()
       play_beep()
       display.clear()