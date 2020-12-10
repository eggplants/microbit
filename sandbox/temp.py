from microbit import *
while True:
    temp = "{:02d}".format(temperature())
    display.scroll(temp)
    black_square = Image("".join(["9"*5+":" for _ in range(5)]))
    display.show(black_square)
    sleep(500)