"""M5STACK CORE 320x240 (ILI9342)
"""

from machine import Pin, SPI
import st7789py as st7789

TFA = 0
BFA = 0
WIDE = 0
TALL = 1
SCROLL = 0      # orientation for scroll.py
FEATHERS = 1    # orientation for feathers.py

def config(rotation=0):
    """Configure the M5Stack CORE display using a custom_init and
        custom_rotations since the display is ili9342c. The custom_init is a
        list of commands to send to the display during the init() metehod. The
        list contains tuples with a bytes object, optionally followed by a
        delay specified in ms. The first byte of the bytes object contains the
        command to send optionally followed by data bytes.
    """

    custom_init = (
        (b'\x11', None, 150),	               # exit sleep
        (b'\xCB', b'\x39\x2C\x00\x34\x02', 0), # power control A
        (b'\xCF', b'\x00\xC1\x30', 0),		   # power control B
        (b'\xE8', b'\x85\x00\x78', 0),		   # driver timing control A
        (b'\xEA', b'\x00\x00', 0),			   # driver timing control B
        (b'\xED', b'\x64\x03\x12\x81', 0),	   # power on sequence control
        (b'\xF7', b'\x20', 0),			       # pump ratio control
        (b'\xC0', b'\x23', 0),			       # power control,VRH[5:0]
        (b'\xC1', b'\x10', 0),			       # Power control,SAP[2:0];BT[3:0]
        (b'\xC5', b'\x3E\x28', 0),			   # vcm control
        (b'\xC7', b'\x86', 0),			       # vcm control 2
        (b'\x3A', b'\x55', 0),			       # pixel format
        (b'\x36', b'\x00', 0),			       # madctl
        (b'\x21', None, 0),			           # inversion on
        (b'\xB1', b'\x00\x18', 0),			   # frameration control,normal mode full colours
        (b'\xB6', b'\x08\x82\x27', 0),		   # display function control
        (b'\xF2', b'\x00', 0),			       # 3gamma function disable
        (b'\x26', b'\x01', 0),			       # gamma curve selected
        # set positive gamma correction
        (b'\xE0', b'\x0F\x31\x2B\x0C\x0E\x08\x4E\xF1\x37\x07\x10\x03\x0E\x09\x00', 0),
        # set negative gamma correction
        (b'\xE1', b'\x00\x0E\x14\x03\x11\x07\x31\xC1\x48\x08\x0F\x0C\x31\x36\x0F', 0),
        (b'\x29', None, 100),                  # display on
    )

    custom_rotations = (
        (0x08, 320, 240, 0, 0, False),
        (0x68, 240, 320, 0, 0, False),
        (0xc8, 320, 240, 0, 0, False),
        (0xa8, 240, 320, 0, 0, False),
    )

    return st7789.ST7789(
        SPI(2, baudrate=40000000, sck=Pin(18), mosi=Pin(23)),
        320,
        240,
        reset=Pin(33, Pin.OUT),
        cs=Pin(14, Pin.OUT),
        dc=Pin(27, Pin.OUT),
        backlight=Pin(32, Pin.OUT),
        custom_init=custom_init,
        custom_rotations=custom_rotations,
        rotation=rotation)
