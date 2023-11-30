.. _write_font_converter:

write_font_converter.py
-----------------------
Convert characters from a truetype font to a python bitmap for use with the bitmap or write method.
The chango, noto_fonts and proverbs examples use converted TrueType fonts.

.. seealso::
    - :ref:`chango.py<chango>`.
    - :ref:`noto_fonts.py<noto_fonts>`.
    - :ref:`proverbs.py<proverbs>`.

Example
^^^^^^^

.. code-block:: console

    # convert the Chango-Regular.ttf to a python bitmap module with approximately 32 pixel high characters
    ./write_font_converter.py Chango-Regular.ttf 32 -c 0x20-0x7f > chango_32.py

.. code-block:: python

    import tft_config
    import chango_32
    tft = tft_config.config(1)
    tft.write(chango_32, "Hello World!", 0, 0)

Usage
^^^^^

.. code-block:: console

    usage: write_font_converter.py [-h] [-width FONT_WIDTH] (-c CHARACTERS | -s STRING) font_file font_height

    Convert characters from a truetype font to a python bitmap for use with the bitmap method in the st7789 and ili9342 drivers.

    positional arguments:
    font_file             name of font file to convert.
    font_height           size of font to create bitmaps from.

    optional arguments:
    -h, --help            show this help message and exit
    -width FONT_WIDTH, --font_width FONT_WIDTH
                            width of font to create bitmaps from.

    character selection:
    characters from the font to include in the bitmap.

    -c CHARACTERS, --characters CHARACTERS
                            integer or hex character values and/or ranges to include. For example: "65, 66, 67" or "32-127" or "0x30-0x39,
                            0x41-0x5a"
    -s STRING, --string STRING
                            string of characters to include For example: "1234567890-."

