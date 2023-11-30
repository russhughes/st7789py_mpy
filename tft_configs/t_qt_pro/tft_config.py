"""LilyGo T-QT Pro 128x128 (GC9107)

https://www.lilygo.cc/products/t-qt-pro

"""

from machine import Pin, SPI
import st7789py as st7789

TFA = 1
BFA = 3
WIDE = 2
TALL = 3
SCROLL = 0      # orientation for scroll.py
FEATHERS = 1    # orientation for feathers.py

def config(rotation=0):
    """
    Configures and returns an instance of the ST7789 display driver.

    Args:
        rotation (int): The rotation of the display (default: 0).

    Returns:
        ST7789: An instance of the ST7789 display driver.
    """

    custom_rotations = (
        (0x00, 128, 128, 2, 1, False),
        (0x60, 128, 128, 1, 2, False),
        (0xc0, 128, 128, 2, 1, False),
        (0xa0, 128, 128, 1, 2, False),
    )

    return st7789.ST7789(
        SPI(2, baudrate=40000000, sck=Pin(3), mosi=Pin(2), miso=None),
        128,
        128,
        reset=Pin(1, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(6, Pin.OUT),
        #backlight=Pin(10, Pin.OUT),
        rotation=rotation,
        custom_rotations=custom_rotations,
        color_order=st7789.BGR
    )
