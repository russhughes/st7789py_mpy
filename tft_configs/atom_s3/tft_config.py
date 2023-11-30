"""M5STACK AtomS3 128x128 (GC9107)

https://docs.m5stack.com/en/core/AtomS3

"""

from machine import Pin, SPI
import st7789py as st7789

TFA = 1
BFA = 3
WIDE = 1
TALL = 0
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

    return st7789.ST7789(
        SPI(2, baudrate=40000000, sck=Pin(17), mosi=Pin(21), miso=None),
        128,
        128,
        reset=Pin(34, Pin.OUT),
        cs=Pin(15, Pin.OUT),
        dc=Pin(33, Pin.OUT),
        backlight=Pin(16, Pin.OUT),
        rotation=rotation,
        color_order=st7789.BGR,
    )
