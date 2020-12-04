from microbit import *
from random import randint
import music
import speech

def is_dark():
    return display.read_light_level() < 10

def sleep_second(sec=1):
    sleep(sec*1000)

def rand_startime():
    return 10 * randint(0, 9) + 30

def play_normal_music(source=music.CHASE):
    music.play(source, wait=False, loop=True)

def play_startime_music(source=music.NYAN):
    music.play(source, wait=False, loop=True)

def play_win_music(source=music.ENTERTAINER):
    music.play(source * 3, wait=True)

def play_lose_music(source=music.FUNERAL):
    music.play(source * 3, wait=True)

def say_chaser_win():
    speech.say("Chaser win!")
    sleep(500)
    speech.say("Chaserer lose!")

def say_chaser_lose():
    speech.say("Chaser lose!")
    sleep(500)
    speech.say("Chaserer win!")

show_yes = lambda: display.show(Image.YES)
show_no = lambda: display.show(Image.NO)

class Motor(object):
    def __init__(self, pinvref, pin1, pin2):
        self.pinvref = pinvref
        self.pin1 = pin1
        self.pin2 = pin2じ

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

# Start with the can set
"""
TODO:
    - 人数を入力して時間を設定
    - ゲームの開始をボタンで制御
    - モータの制御
"""
is_end = False
while True:

    # normal
    show_no()
    play_normal_music()
    for _ in range(rand_startime() + 30):
        if not is_dark():
            play_lose_music();say_chaser_win()
            is_end = True
            break
        sleep_second(1)
    if is_end:
        music.stop()
        break

    # star
    show_yes()
    play_startime_music()
    for _ in range(rand_startime()):
        if not is_dark():
            play_win_music();say_chaser_lose()
            is_end = True
            break
        sleep_second(1)
    if is_end:
        music.stop()
        break

display.clear()