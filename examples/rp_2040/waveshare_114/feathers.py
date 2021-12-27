"""
feathers.py

    Smoothly scroll mirrored rainbow colored random curves across the display.

"""

import random
import math
import utime
from machine import Pin, SoftSPI
import st7789py as st7789


def between(left, right, along):
    """returns a point along the curve from left to right"""
    dist = (1 - math.cos(along * math.pi)) / 2
    return left * (1 - dist) + right * dist


def color_wheel(position):
    """returns a 565 color from the given position of the color wheel"""
    position = (255 - position) % 255

    if position < 85:
        return st7789.color565(255 - position * 3, 0, position * 3)

    if position < 170:
        position -= 85
        return st7789.color565(0, position * 3, 255 - position * 3)

    position -= 170
    return st7789.color565(position * 3, 255 - position * 3, 0)


def main():
    '''
    The big show!
    '''
    #enable display and clear screen

    tft = st7789.ST7789(
            SoftSPI(baudrate=30000000, polarity=1, sck=Pin(10), mosi=Pin(11), miso=Pin(16)),
            135,
            240,
            reset=Pin(12, Pin.OUT),
            cs=Pin(9, Pin.OUT),
            dc=Pin(8, Pin.OUT),
            backlight=Pin(13, Pin.OUT),
            rotation=1)

    tft.fill(st7789.BLACK)      # clear screen

    height = tft.height         # height of display in pixels
    width = tft.width           # width if display in pixels

    tfa = 40                    # top free area when scrolling
    bfa = 40        	        # bottom free area when scrolling

    scroll = 0                  # scroll position
    wheel = 0                   # color wheel position

    tft.vscrdef(tfa, width, bfa)    # set scroll area
    tft.vscsad(scroll + tfa)        # set scroll position
    tft.fill(st7789.BLACK)          # clear screen

    half = (height >> 1) - 1    # half the height of the dislay
    interval = 0                # steps between new points
    increment = 0               # increment per step
    counter = 1                 # step counter, overflow to start
    current_y = 0               # current_y value (right point)
    last_y = 0                  # last_y value (left point)

    # segment offsets
    x_offsets = [x * (width // 8) -1 for x in range(2,9)]

    while True:
        # when the counter exceeds the interval, save current_y to last_y,
        # choose a new random value for current_y between 0 and 1/2 the
        # height of the display, choose a new random interval then reset
        # the counter to 0

        if counter > interval:
            last_y = current_y
            current_y = random.randint(0, half)
            counter = 0
            interval = random.randint(10, 100)
            increment = 1/interval      # increment per step

        # clear the first column of the display and scroll it
        tft.vline(scroll, 0, height, st7789.BLACK)
        tft.vscsad(scroll + tfa)

        # get the next point between last_y and current_y
        tween = int(between(last_y, current_y, counter * increment))

        # draw mirrored pixels across the display at the offsets using the color_wheel effect
        for i, x_offset in enumerate(x_offsets):
            tft.pixel((scroll + x_offset) % width, half + tween, color_wheel(wheel+(i<<2)))
            tft.pixel((scroll + x_offset) % width, half - tween, color_wheel(wheel+(i<<2)))

        # increment scroll, counter, and wheel
        scroll = (scroll + 1) % width
        wheel = (wheel + 1) % 256
        counter += 1

main()
