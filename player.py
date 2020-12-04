import music
from microbit import *

play_lis = [eval("['{}',music.{}]".format(song, song))
            for song in dir(music) if song.isupper()]


def player(play_lis):
    lis_len, now_ind, end_play = len(play_lis), 0, False
    while True:
        if end_play:
            break
        name, source = play_lis[now_ind]
        display.scroll(name, wait=False, loop=True)
        music_len = len(source) - 1
        for ind, sound in enumerate(source):
            music.play(sound)
            if button_a.is_pressed() and button_b.is_pressed():
                end_play = True
                break
            elif button_a.is_pressed():
                now_ind -= 1
                break
            elif button_b.is_pressed():
                now_ind = (now_ind + 1) % lis_len
                break
            if ind == music_len:
                now_ind = (now_ind + 1) % lis_len


display.scroll("PRESS A+B TO PLAY", wait=False, loop=True)
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        player(play_lis)