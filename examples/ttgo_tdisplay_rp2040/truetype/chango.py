"""
chango.py

    Test for font2bitmap converter for the driver.
    See the font2bitmap program in the utils directory.
"""

from machine import Pin, SoftSPI
import st7789py as st7789
import gc
from truetype import chango_16 as font_16
from truetype import chango_32 as font_32
from truetype import chango_64 as font_64

gc.collect()


def main():
    # enable display and clear screen
    spi = SoftSPI(
        baudrate=20000000,
        polarity=1,
        phase=0,
        sck=Pin(18),
        mosi=Pin(19),
        miso=Pin(13))

    tft = st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(23, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=1)

    tft.fill(st7789.BLACK)

    row = 0
    tft.write(font_16, "abcdefghijklmnopqrst", 0, row, st7789.RED)
    row += font_16.HEIGHT

    tft.write(font_32, "abcdefghij", 0, row, st7789.GREEN)
    row += font_32.HEIGHT

    tft.write(font_64, "abcd", 0, row, st7789.BLUE)
    row += font_64.HEIGHT


main()
