#!/usr/bin/env python
#
# !!! Needs psutil (+ dependencies) installing:
#
#    $ sudo apt-get install python-dev
#    $ sudo pip install psutil
#

import os
import sys
import fluidsynth

if os.name != 'posix':
    sys.exit('platform not supported')
import psutil

fs = fluidsynth.Synth()

from datetime import datetime
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont

# TODO: custom font bitmaps for up/down arrows
# TODO: Load histogram

def test_text(oled):
    font = ImageFont.load_default()
    font2 = ImageFont.truetype('../fonts/mobitec.ttf', 6)
    with canvas(oled) as draw:
        draw.text((0, 0), "Line 1....", font=font2, fill=255)
        draw.text((0, 7), "Line 2....", font=font2, fill=255)
        draw.text((0, 15), "Line 3....", font=font2, fill=255)
        draw.text((0, 23), "Line 4....", font=font2, fill=255)
        draw.text((0, 31), "Line 5....", font=font2, fill=255)
        draw.text((0, 39), "Line 6....", font=font2, fill=255)
        draw.text((0, 47), "Line 7....", font=font2, fill=255)
        draw.text((0, 55), "Line 8....", font=font2, fill=255)

def main():
    oled = ssd1306(port=0, address=0x3C)
    test_text(oled)

if __name__ == "__main__":
    main()
