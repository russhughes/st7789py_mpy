"""
feathers.py

    Smoothly scroll mirrored rainbow colored random curves across the display.

"""

import random
import math
import time
from machine import Pin, SPI
import st7789py as st7789
import vga1_8x8 as font


def center_on(display, font, text, y, fg, bg):
    '''
    Center the text on the display
    '''
    x = (display.width - len(text) * font.WIDTH) // 2
    display.text(font, text, x, y, fg, bg)

def main():
    '''
    The big show!
    '''
    #enable display and clear screen

    spi = SPI(2, baudrate=40000000, sck=Pin(17), mosi=Pin(21), miso=None)
    tft = st7789.ST7789(
        spi,
        128,
        128,
        reset=Pin(34, Pin.OUT),
        cs=Pin(15, Pin.OUT),
        dc=Pin(33, Pin.OUT),
        backlight=Pin(16, Pin.OUT),
        rotation=1,
        color_order=st7789.BGR)

    height = tft.height         # height of display in pixels
    width = tft.width           # width if display in pixels

    while True:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(st7789.BLACK)
            tft.rect(0, 0, width, height, st7789.RED)
            center_on(tft, font, "Rotation", height // 2 - font.HEIGHT, st7789.WHITE, st7789.BLACK)
            center_on(tft, font, str(rotation), height // 2 + font.HEIGHT, st7789.WHITE, st7789.BLACK)
            time.sleep(1)

main()
