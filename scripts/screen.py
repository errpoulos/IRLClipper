import time
import math
import os
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import textwrap
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


def writeToScreen(messageType, message, optional):
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)
    disp.begin()

    disp.clear()
    disp.display()

    # Create blank screen to draw on
    width = disp.width
    height = disp.height

    # Create image with mode '1' for 1-bit color.
    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    #Define constants
    padding = 0
    top = padding
    bottom = height-padding
    x = padding

    # Load default font.
    font = ImageFont.load_default()

    # Two lines of text that wrap at the edge of the screen. Top line is messageType, bottom line is message
    lines = textwrap.wrap(message, width=20)
    y_text = 20
    w = 1 # we'll always start at left side of OLED
    draw.text((x, top), messageType,  font=font, fill=255)
    draw.text((x, top+40), optional,  font=font, fill=255)


    for line in lines:
        width, height = font.getsize(line)
        draw.text((w, y_text), line, font=font, fill=1)
        y_text += height
        # Display text.
        disp.image(image)
        disp.display()

    # time.sleep(5)
    # disp.begin()

    # disp.clear()
    # disp.display()
    # 