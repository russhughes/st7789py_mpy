"""LilyGo T-embed 170x320
"""

from machine import Pin, SPI
import st7789py as st7789


TFA = 0
BFA = 0
WIDE = 1
TALL = 0
SCROLL = 0      # orientation for scroll.py
FEATHERS = 1    # orientation for feathers.py

POWER = Pin(46, Pin.OUT, value=1)

def config(rotation=0):
    """
    Configures and returns an instance of the ST7789 display driver.

    Args:
        rotation (int): The rotation of the display (default: 0).

    Returns:
        ST7789: An instance of the ST7789 display driver.
    """

    custom_rotations = (
        (0x00, 170, 320, 35, 0, False),
        (0x60, 320, 170, 0, 35, False),
        (0xC0, 170, 320, 35, 0, False),
        (0xA0, 320, 170, 0, 35, False),
    )

    return st7789.ST7789(
        SPI(2, baudrate=40000000, sck=Pin(12), mosi=Pin(11), miso=None),
        170,
        320,
        cs=Pin(10, Pin.OUT),
        dc=Pin(13, Pin.OUT),
        reset=Pin(9, Pin.OUT),
        backlight=Pin(15, Pin.OUT),
        custom_rotations=custom_rotations,
        rotation=rotation,
        color_order=st7789.BGR,
    )
