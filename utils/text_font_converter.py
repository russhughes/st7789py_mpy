#!/usr/bin/env python3
"""
Convert fonts from the font-bin directory of spacerace's https://github.com/spacerace/romfont
VGA and BIOS rom font repo.  Optionally limiting the characters included to -first-char (-f) thru
-last-char (-l).

Input can be a file or a directory containing multiple font files. If input is a directory, output
must also be a directory.  If input is a file, output can be a file or a directory.

.. seealso::
    - :ref:`color_test.py<color_test>`.
    - :ref:`fonts.py<fonts>`.
    - :ref:`hello.py<hello>`.
    - :ref:`rotations.py<rotations>`.
    - :ref:`scroll.py<scroll>`.
    - :ref:`tiny_toasters.py<tiny_toasters>`.

Example
^^^^^^^

.. code-block:: console

    # convert the IBM_VGA_8x8.bin font to a python module with 8x8 characters
    text_font_converter.py romfont/font-bin/IBM_VGA_8x8.bin vga_8x8.py -f 32 -l 127

.. code-block:: python

    import tft_config
    import vga_8x8
    tft = tft_config.config(1)
    tft.bitmap(vga_8x8, "Hello World!", 0, 0)

Usage
^^^^^

.. code-block:: console

    usage: text_font_converter.py [-h] [-f FIRST_CHAR] [-l LAST_CHAR] input output

    Convert romfont.bin file or directory to python module(s).

    positional arguments:
    input                 file or directory containing binary font file(s).
    output                file or directory to contain python font file(s).

    optional arguments:
    -h, --help            show this help message and exit
    -f FIRST_CHAR, --first-char FIRST_CHAR
                            The first character code to include in the conversion (default: 0x20).
    -l LAST_CHAR, --last-char LAST_CHAR
                            The last character code to include in the conversion (default: 0x7F).

"""

import os
import re
import argparse


def convert_font(file_in, file_out, width, height, first=0x0, last=0xFF):
    """
    Convert a font file to a python font file.

    Args:
        file_in (str): Path to the input font file or directory to convert.
        file_out (str): Path to the output python font file or directory.
        width (int): Width of the font.
        height (int): Height of the font.
        first (int): The first character code to include in the conversion (default: 0x0).
        last (int): The last character code to include in the conversion (default: 0xFF).

    Returns:
        None

    """
    chunk_size = height
    with open(file_in, "rb") as bin_file, open(
        file_out, "wt", encoding="utf-8"
    ) as font_file:
        bin_file.seek(first * height)
        print(f'# converted from {file_in}\n\n_FONT =\\', file=font_file)

        for i in range(first, last + 1):
            chunk = bin_file.read(chunk_size)
            if not chunk:
                last = i - 1
                break

            font_data = "".join(f"\\x{byte:02x}" for byte in chunk)
            print(f"b'{font_data}'\\", file=font_file)

        print(
            "\n"
            f"WIDTH = {width}\n"
            f"HEIGHT = {height}\n"
            f"FIRST = 0x{first:02x}"
            f"LAST = 0x{last:02x}",
            "\nFONT = memoryview(_FONT)",
            file=font_file,
        )


def main():
    """
        Convert fomfont.bin font file(s) in input to python module(s) in output.

    Args:
        input (str): File or directory containing binary font file(s).
        output (str): File or directory to contain python font file(s).
        first_char (int): The first character code to include in the conversion (default: 0x20).
        last_char (int): The last character code to include in the conversion (default: 0x7F).
    """

    parser = argparse.ArgumentParser(
        description="Convert romfont.bin file or directory to python module(s)."
    )
    parser.add_argument(
        "input", help="file or directory containing binary font file(s)."
    )
    parser.add_argument(
        "output", help="file or directory to contain python font file(s)."
    )
    parser.add_argument(
        "-f",
        "--first-char",
        type=lambda x: int(x, 0),
        default=0x20,
        help="The first character code to include in the conversion (default: 0x20).",
    )

    parser.add_argument(
        "-l",
        "--last-char",
        type=lambda x: int(x, 0),
        default=0x7F,
        help="The last character code to include in the conversion (default: 0x7F).",
    )

    args = parser.parse_args()

    file_re = re.compile(r"^(.*)(\d+)x(\d+)\.bin$")
    is_dir = os.path.isdir(args.input)
    bin_files = os.listdir(args.input) if is_dir else [args.input]

    for bin_file_name in bin_files:
        if match := file_re.match(bin_file_name):
            font_width = int(match[2])
            font_height = int(match[3])
            base_name = match[1].rstrip("_").lower()
            font_file_name = f"{base_name}_{font_width}x{font_height}.py"
            if is_dir:
                bin_file_name = os.path.join(args.input, bin_file_name)
                font_file_name = os.path.join(args.output, font_file_name)
            else:
                font_file_name = args.output

            print("converting", bin_file_name, "to", font_file_name)
            convert_font(
                bin_file_name,
                font_file_name,
                font_width,
                font_height,
                args.first_char,
                args.last_char,
            )


if __name__ == "__main__":
    main()
