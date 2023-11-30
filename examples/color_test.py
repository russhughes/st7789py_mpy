"""
color_test.py
=============

.. figure:: ../_static/color_test.jpg
    :align: center

    Test color with gradients.

Draws Red, Green and Blues gradients on the display and writes the color name centered in the
gradient.  Then repeatedly draws a borders around the display in the same colors.

.. note:: This example requires the following modules:

  .. hlist::
    :columns: 3

    - `st7789py`
    - `tft_config`
    - `vga2_bold_16x32`

"""

import random
from machine import Pin, SoftSPI
from time import sleep
import st7789py as st7789
import tft_config
import vga2_bold_16x32 as font


def interpolate(value1, value2, position, total_range):
    """
    Perform linear interpolation between two values based on a position within a range.

    Args:
        value1 (float): Starting value.
        value2 (float): Ending value.
        position (float): Current position within the range.
        total_range (float): Total range of positions.

    Returns:
        float: Interpolated value.
    """
    return value1 + (value2 - value1) * position / total_range


def main():
    tft = tft_config.config(tft_config.WIDE)

    names = ["Red", "Green", "Blue"]

    color_values = (255, 255, 255)
    height_division = tft.height // len(color_values)
    for i, color_value in enumerate(color_values):
        start_row = i * height_division
        end_row = (i + 1) * height_division
        for row in range(start_row, end_row):
            rgb_color = [0 if idx != i else int(interpolate(0, color_value, row - start_row, height_division)) for idx in range(3)]
            color = st7789.color565(rgb_color)
            tft.hline(0, row, tft.width, color)

        name = names[i]
        text_x = (tft.width - font.WIDTH * len(name)) // 2
        text_y = start_row + (end_row - start_row - font.HEIGHT) // 2
        tft.text(font, name, text_x, text_y, st7789.WHITE, color)

    while True:
        for color in [st7789.RED, st7789.GREEN, st7789.BLUE]:
            for x in range(tft.width):
                tft.pixel(x, 0, color)
                tft.pixel(x, tft.height - 1, color)

            for y in range(tft.height):
                tft.pixel(0 , y, color)
                tft.pixel(tft.width - 1, y, color)

            sleep(1)
main()
