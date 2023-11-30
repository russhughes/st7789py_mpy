.. _text_font_converter:

text_font_converter.py
----------------------
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

