#!/usr/bin/env python3

"""
Reads all font-bin files from the specified `input` directory and writes png images to t
he specified `output` directory. Optionally limiting the characters included to -first-char
(-f) thru -last-char (-l).  This is the program I used to create the png font samples in the
documentation.

.. seealso::
   - :ref:`Bitmap Font Samples<bitmap-font-samples>`.

Example
^^^^^^^

.. code-block:: console

    - create_png_examples.py font_directory png_directory

Usage
^^^^^

.. code-block:: console

    usage: create_png_examples.py [-h] input output

    Creates png samples of each text font file from the input directoryto the output directory.

    positional arguments:
    input       input directory containing font-bin files
    output      output directory to create pngs

    optional arguments:
    -h, --help  show this help message and exit

"""

import os
import importlib
import argparse
import png


def create_png(font_file_name, png_file_name):
    """
    Convert image file to python module for use with bitmap method.

    Args:
        image_file (str): Name of file containing image to convert.
        bits_per_pixel (int): The number of bits to use per pixel (1..8).

    """

    module_spec = importlib.util.spec_from_file_location("font", font_file_name)
    font = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(font)
    char_count = font.LAST - font.FIRST
    column_count = 16
    row_count = char_count // column_count

    with open(png_file_name, "wb") as png_file:
        image = png.Writer(
            (16 + 2) * font.WIDTH, (row_count + 3) * font.HEIGHT, bitdepth=1
        )
        image_data = [
            [0 for _ in range((16 + 2) * font.WIDTH)]
            for _ in range((row_count + 3) * font.HEIGHT)
        ]
        #font_count = len(font.FONT) + 1
        for chart_row in range(row_count + 2):
            for chart_col in range(16):
                chart_idx = chart_row * 16 + chart_col
                for char_line in range(font.HEIGHT):
                    for char_byte in range(font.WIDTH // 8):
                        ch_idx = (
                            chart_idx * font.HEIGHT * font.WIDTH // 8
                            + char_byte
                            + char_line * font.WIDTH // 8
                        )
                        print(chart_idx, char_count)
                        data = font.FONT[ch_idx] if chart_idx <= char_count else 0
                        for bit in range(8):
                            png_row = (chart_row + 1) * font.HEIGHT + char_line
                            png_col = (chart_col + 1) * font.WIDTH + char_byte * 8 + bit
                            image_data[png_row][png_col] = 1 if data & 1 << 7 - bit else 0

        print("Creating", png_file_name)
        image.write(png_file, image_data)


def main():
    """
    Creates PNG samples of each text font file from the input directory to the output directory.

    Args:
        input (str): Input directory containing font-bin files.
        output (str): Output directory to create PNGs.

    """

    parser = argparse.ArgumentParser(
        description=(
            "Creates png samples of each text font file from the input directory"
             "to the output directory."
        )
    )
    parser.add_argument("input", help="input directory containing font-bin files")
    parser.add_argument("output", help="output directory to create pngs")
    args = parser.parse_args()

    for file_name in os.listdir(args.input):
        if file_name.endswith(".py"):
            font_file_name = os.path.join(args.input, file_name)
            png_file_name = os.path.join(
                args.output, f"{os.path.splitext(file_name)[0]}.png"
            )
            create_png(font_file_name, png_file_name)


if __name__ == "__main__":
    main()
