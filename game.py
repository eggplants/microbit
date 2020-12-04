from random import randint

import music
import speech
from microbit import *


def is_dark() -> bool:
    """Check if amount of light is eq of darkness."""
    return display.read_light_level() < 10


def sleep_second(sec: int = 1) -> None:
    """Sleep given n sec."""
    sleep(sec*1000)


def rand_startime() -> int:
    """Return rand time for unbeatable time."""
    return 10 * randint(0, 9) + 30


def play_normal_music(source=music.CHASE):
    """Play bgm for normal time."""
    music.play(source, wait=False, loop=True)


def play_startime_music(source=music.NYAN):
    """Play bgm for normal time."""
    music.play(source, wait=False, loop=True)


def play_win_music(source=music.ENTERTAINER):
    """Play bgm for win."""
    music.play(source * 3, wait=True)


def play_lose_music(source=music.FUNERAL):
    """Play bgm for lose."""
    music.play(source * 3, wait=True)


def say_chaser_win() -> None:
    """Say 'Chaser win!' and 'Chaserer lose!'."""
    speech.say("Chaser win!")
    sleep(500)
    speech.say("Chaserer lose!")


def say_chaser_lose() -> None:
    """Say 'Chaser lose!' and 'Chaserer win!'."""
    speech.say("Chaser lose!")
    sleep(500)
    speech.say("Chaserer win!")


def wait_presskey() -> None:
    """"""
    while True:
        if button_a.is_pressed() or button_b.is_pressed():
            break


def show_yes(): return display.show(Image.YES)
def show_no(): return display.show(Image.NO)


class Motor(object):
    def __init__(self, pinvref, pin1, pin2):
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

# Start with the can set


"""
TODO:
    - 人数を入力して時間を設定
    - モータの制御
"""


def main():

    is_end = False
    while True:

        # normal
        show_no()
        play_normal_music()
        for _ in range(rand_startime() + 30):
            if not is_dark():
                play_lose_music()
                say_chaser_win()
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
                play_win_music()
                say_chaser_lose()
                is_end = True
                break
            sleep_second(1)
        if is_end:
            music.stop()
            break

    display.clear()


if __name__ == "__main__":
    is_scroll = False
    while True:
        # Control the start of the game with a button
        display.scroll("PRESS ANY KEY", wait=False, loop=True)
        wait_presskey()
        music.play(music.POWER_UP)
        main()
