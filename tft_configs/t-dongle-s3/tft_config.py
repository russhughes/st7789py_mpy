"""LilyGo T-Dongle-S3 80x160 (ST7735)
"""

from machine import Pin, SPI
import st7789py as st7789


TFA = 1
BFA = 1
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

    init_cmds = (
        (b'\xCF', b'\x00\x83\x30', 0),
        (b'\xED', b'\x64\x03\x12\x81', 0),
        (b'\xE8', b'\x85\x01\x79', 0),
        (b'\xCB', b'\x39\x2C\x00\x34\x02', 0),
        (b'\xF7', b'\x20', 0),
        (b'\xEA', b'\x00\x00', 0),
        (b'\xC0', b'\x26', 0),
        (b'\xC1', b'\x11', 0),
        (b'\xC5', b'\x35\x3E', 0),
        (b'\xC7', b'\xBE', 0),
        (b'\x3A', b'\x55', 0),
        (b'\xB1', b'\x00\x1B', 0),
        (b'\xF2', b'\x08', 0),
        (b'\x26', b'\x01', 0),
        (b'\xE0', b'\x1F\x1A\x18\x0A\x0F\x06\x45\x87\x32\x0A\x07\x02\x07\x05\x00', 0),
        (b'\xE1', b'\x00\x25\x27\x05\x10\x09\x3A\x78\x4D\x05\x18\x0D\x38\x3A\x1F', 0),
        (b'\x2A', b'\x00\x00\x00\xEF', 0),
        (b'\x2B', b'\x00\x00\x01\x3f', 0),
        (b'\x2C', None, 0),
        (b'\xB7', b'\x07', 0),
        (b'\xB6', b'\x0A\x82\x27\x00', 0),
        (b'\x21', None, 0),
        (b'\x11', None, 100),
        (b'\x29', None, 100)
    )

    custom_rotations = (
        (0x00,  80, 160, 26,  1, False),
        (0x60, 160,  80,  1, 26, False),
        (0xc0,  80, 160, 26,  1, False),
        (0xa0, 160,  80,  1, 26, False),
    )

    return st7789.ST7789(
        SPI(1, baudrate=20000000, sck=Pin(5), mosi=Pin(3), miso=None),
        80,
        160,
        reset=Pin(1, Pin.OUT),
        cs=Pin(4, Pin.OUT),
        dc=Pin(2, Pin.OUT),
        backlight=Pin(37, Pin.OUT),
        rotation=rotation,
        color_order=st7789.BGR,
        custom_init=init_cmds,
        custom_rotations=custom_rotations,
    )
