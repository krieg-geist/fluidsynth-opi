from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont, ImageDraw

device = ssd1306(port=3, address=0x3C)  # rev.1 users set port=0
draw = canvas(device)    
font = ImageFont.load_default()
draw.rectangle((0, 0, 40, 40), outline=255, fill=255)
draw.line((0,0 , 20 , 20 ), fill="white")
