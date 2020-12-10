from motor import Motor
from microbit import *
import music

m=Motor(pin0, pin12, pin13)

def count_ntimes(n):
    for _ in range(n):
           display.show(_)
           sleep(1000)

def play_beep():
    music.play(music.BA_DING, pin=pin8)

display.scroll("waiting...", wait=False)
while True:
   if button_a.is_pressed():
       m.start_forward(speed=500)
       count_ntimes(5)
       m.stop()
       play_beep()
       display.clear()
   if button_b.is_pressed():
       m.start_backward(speed=500)
       count_ntimes(5)
       m.stop()
       play_beep()
       display.clear()
