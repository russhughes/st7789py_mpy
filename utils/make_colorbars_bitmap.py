#!/usr/bin/env python3
"""
Create a MicroPython bitmap module with WHITE, YELLOW, CYAN, GREEN, MAGENTA, RED, and BLUE
color bars for testing. Use redirection to save the output to a file.  The bitmap is saved
as a python module that can be imported and used with the bitmap method.

.. seealso::
  :ref:`colorbars.py<colorbars>`.

Example
^^^^^^^

.. code-block:: console

    ./make_colorbars_bitmap.py 320 240 3 > colorbars_bitmap320x240.py

The python file can be imported and displayed with the bitmap method. For example:

.. code-block:: python

    import tft_config
    import colorbars_bitmap320x240
    tft = tft_config.config(1)
    tft.bitmap(colorbars_bitmap320x240, 0, 0)

Usage
^^^^^

.. code-block:: console

usage: make_colorbars_bitmap.py [-h] [--png png] width height bits_per_pixel

Create a bitmap module with color bars for use with the bitmap method.

positional arguments:
  width           The width of the image in pixels
  height          The height of the image in pixels
  bits_per_pixel  The number of bits to use per pixel (1..8)

optional arguments:
  -h, --help      show this help message and exit
  --png png       Optionally create png file

"""

import sys
from PIL import Image, ImageDraw
import argparse


def main():

    parser = argparse.ArgumentParser(
        description='Create a bitmap module with color bars for use with the bitmap method.')

    parser.add_argument(
        'width',
        type=int,
        default=320,
        help='The width of the image in pixels')

    parser.add_argument(
        'height',
        type=int,
        default=240,
        help='The height of the image in pixels')

    parser.add_argument(
        'bits_per_pixel',
        type=int,
        choices=range(1, 9),
        default=3,
        metavar='bits_per_pixel',
        help='The number of bits to use per pixel (1..8)')

    parser.add_argument(
        '--png',
        type=str,
        default=None,
        metavar='png',
        help='Optionally create png file')

    args = parser.parse_args()
    bits = args.bits_per_pixel
    colors_requested = 1 << bits
    img = Image.new(mode = "RGB", size = (args.width, args.height) )

    # Define the colors
    colors = ["WHITE", "YELLOW", "CYAN", "GREEN", "MAGENTA", "RED", "BLUE"]

    # Calculate the width of each box
    box_width = args.width // len(colors)

    # Create a draw object
    draw = ImageDraw.Draw(img)

    # Draw the boxes
    for i, color in enumerate(colors):
        start = i * box_width
        end = start + box_width
        draw.rectangle([(start, 0), (end, args.height)], fill=color)

    # Remove the draw object
    del draw

    img = img.convert("P", palette=Image.Palette.ADAPTIVE, colors=colors_requested)
    if args.png:
        img.save(args.png)

    palette = img.getpalette()  # Make copy of palette colors
    palette_colors = len(palette) // 3
    bits_required = palette_colors.bit_length()
    if (bits_required < bits):
        print(f'\nNOTE: Quantization reduced colors to {palette_colors} from the {colors_requested} '
        f'requested, reconverting using {bits_required} bit per pixel could save memory.\n''', file=sys.stderr)

    # For all the colors in the palette
    colors = []

    for color in range(colors_requested):

        # get rgb values and convert to 565
        color565 = (
            ((palette[color*3] & 0xF8) << 8)
            | ((palette[color*3+1] & 0xFC) << 3)
            | ((palette[color*3+2] & 0xF8) >> 3))

        # append byte swapped 565 color to colors
        colors.append(f'{color565:04x}')

    image_bitstring = ''
    max_colors = len(colors)

    # Run through the image and create a string with the ascii binary
    # representation of the color of each pixel.
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            color = pixel
            bstring = ''.join(
                '1' if (color & (1 << bit - 1)) else '0'
                for bit in range(bits, 0, -1)
            )

            image_bitstring += bstring

    bitmap_bits = len(image_bitstring)

    # Create python source with image parameters
    print(f'HEIGHT = {img.height}')
    print(f'WIDTH = {img.width}')
    print(f'COLORS = {max_colors}')
    print(f'BITS = {bitmap_bits}')
    print(f'BPP = {bits}')
    print('PALETTE = [', sep='', end='')

    for color, rgb in enumerate(colors):
        if color:
            print(',', sep='', end='')
        print(f'0x{rgb}', sep='', end='')
    print("]")

    # Run though image bit string 8 bits at a time
    # and create python array source for memoryview

    print("_bitmap =\\", sep='')
    print("b'", sep='', end='')

    for i in range(0, bitmap_bits, 8):

        if i and i % (16*8) == 0:
            print("'\\\nb'", end='', sep='')

        value = image_bitstring[i:i+8]
        color = int(value, 2)
        print(f'\\x{color:02x}', sep='', end='')

    print("'\nBITMAP = memoryview(_bitmap)")


main()
