"""
boxlines.py
===========

.. figure:: ../_static/boxlines.jpg
    :align: center

    Test for lines and rectangles.

Draws lines and rectangles in random colors at random locations on the display.

.. note:: This example requires the following modules:

  .. hlist::
    :columns: 3

    - `st7789py`
    - `tft_config`

"""

import random
import tft_config
import st7789py as st7789


def main():
    """ main """
    tft = tft_config.config(tft_config.WIDE)

    while True:
        color = st7789.color565(
            random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)
        )

        tft.line(
            random.randint(0, tft.width),
            random.randint(0, tft.height),
            random.randint(0, tft.width),
            random.randint(0, tft.height),
            color,
        )

        width = random.randint(0, tft.width // 2)
        height = random.randint(0, tft.height // 2)
        col = random.randint(0, tft.width - width)
        row = random.randint(0, tft.height - height)
        tft.fill_rect(
            col,
            row,
            width,
            height,
            st7789.color565(
                random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)
            ),
        )


main()
