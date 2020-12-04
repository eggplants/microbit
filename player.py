from microbit import *
import music

play_lis = [eval("['{}',music.{}]".format(song, song)) for song in dir(music) if song.isupper()]

def player(play_lis):
    lis_len, now_ind, end_play = len(play_lis), 0, False
    while True:
        if end_play:
            break
        display.scroll(play_lis[now_ind][0], wait=False, loop=True)
        for sound in play_lis[now_ind][1]:
            music.play(sound)
            if button_a.is_pressed():
                now_ind -= 1
                break
            elif button_b.is_pressed():
                now_ind = (now_ind + 1) % lis_len
                break
            elif button_a.is_pressed() and button_b.is_pressed():
                end_play = False
                break
        now_ind = (now_ind + 1) % lis_len

while True:
    display.scroll("PRESS A+B TO PLAY", wait=False, loop=True)
    if button_a.is_pressed() and button_b.is_pressed():
        player(play_lis)