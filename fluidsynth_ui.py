#!/usr/bin/env python
#
# !!! Needs psutil (+ dependencies) installing:
#
#    $ sudo apt-get install python-dev
#    $ sudo pip install psutil
#

import os
import sys
import fluidsynth_backend
import sys
from time import sleep

if os.name != 'posix':
    sys.exit('platform not supported')
import psutil

from datetime import datetime
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont

# TODO: custom font bitmaps for up/down arrows
# TODO: Load histogram

def test_text(oled):
    font = ImageFont.load_default()
    font2 = ImageFont.truetype('fonts/mobitec.ttf', 8)
    with canvas(oled) as draw:
        draw.text((0, 0), "Line 1....", font=font2, fill=255)
        draw.text((0, 7), "Line 2....", font=font2, fill=255)
        draw.text((0, 15), "Line 3....", font=font2, fill=255)
        draw.text((0, 23), "Line 4....", font=font2, fill=255)
        draw.text((0, 31), "Line 5....", font=font2, fill=255)
        draw.text((0, 39), "Line 6....", font=font2, fill=255)
        draw.text((0, 47), "Line 7....", font=font2, fill=255)
        draw.text((0, 55), "Line 8....", font=font2, fill=255)

def test_menu():
    from menu import Menu
    from rotary import Rotary

    m = Menu([
        "First line",
        "A second menu option",
        "Now to the third",
        "On to the forth",
        "Follow the fifth",
        "Support the sixth"
    ])

    r = Rotary(**{'menu': m, 'clk': 29, 'dt': 31, 'btn': 37})

    if len(sys.argv) > 1:
        if sys.argv[1] == 'clear':
            m.blank(True)
        else:
            m.set_highlight(int(sys.argv[1]))
            m.render()
    else:
        m.render()

    while True:
        sleep(1)

def main():
    oled = ssd1306(port=3, address=0x3C)
    test_menu()

if __name__ == "__main__":
    main()
