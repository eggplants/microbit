from microbit import *

# sc = lambda s: display.scroll(str(s), wait=False, loop=True, delay=50)
get_light = display.read_light_level
while True:
    if get_light() > 9:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
