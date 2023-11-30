Fonts
=====

The driver supports two different types of fonts: fixed-size bitmap fonts extracted from PC VGA and Bios images and fixed or proportional width fonts converted from True-Type fonts. All fonts are stored in python modules and imported using the standard python import statement.

Pre-compiling the font python modules to .mpy files will significantly reduce the memory required for the fonts. For even more memory savings, the font files can be converted to frozen bytecode and compiled into the MicroPython firmware.

.. list-table:: Comparison of Bitmap and TrueType Fonts Attributes
   :widths: 10 30 30
   :header-rows: 1

   * - Attribute
     - Bitmap Fonts
     - TrueType Fonts
   * - Source
     - PC BIOS images
     - True-Type fonts
   * - Conversion Tool
     - |text_util|
     - write_font_converter.py
   * - Character Sets
     - 128 and 256 PC character sets
     - User defined
   * - Pixel Sizes
     - 8x8, 8x16, 16x6, and 16x32
     - width 256 pixels or less
   * - Rendering Method
     - text() method
     - write() method


Bitmap Fonts
------------

Bitmap fonts are available in 128 and 256 PC character sets in 8x8, 8x16, 16x6 and 16x32 pixel sizes. They are written using the text method.

Bitmap Font Conversion
^^^^^^^^^^^^^^^^^^^^^^

The `utils` directory contains the text_font_converter.py program used to convert PC BIOS bitmap fonts from the font-bin directory of spacerace's https://github.com/spacerace/romfont repo.

The utility converts all romfont bin files in the specified -input-directory (-i) and writes python font files to the specified -output-directory (-o).

Characters included can be limited by using the -first-char (-f) and -last-char (-l) options.

Example:

    text_font_converter.py -i font-bin -o fonts -f 32 -l 127


.. literalinclude:: romfont.py
   :linenos:
   :language: python
   :caption: Sample converted romfont font module.


.. _bitmap-font-samples:

Bitmap Font Samples
^^^^^^^^^^^^^^^^^^^

8x8 Rom Fonts
"""""""""""""

.. figure:: _static/vga1_8x8.png
   :align: center

   vga1_8x8.py: 128 Character 8x8 Font

|

.. figure:: _static/vga2_8x8.png
   :align: center

   vga2_8x8.py: 256 Character 8x8 Font

|

8x16 Rom Fonts
""""""""""""""

.. figure:: _static/vga1_8x16.png
   :align: center

   vga1_8x16.py: 128 Character 8x16 Font

|

.. figure:: _static/vga2_8x16.png
   :align: center

   vga2_8x16.py: 256 Character 8x16 Font

|

16x16 Rom Fonts
"""""""""""""""

.. figure:: _static/vga1_16x16.png
   :align: center

   vga1_16x16.py: 128 Character 16x16 Thin Font

|

.. figure:: _static/vga1_bold_16x16.png
   :align: center

   vga1_bold_16x16.py: 128 Character 16x16 Bold Font

|

.. figure:: _static/vga2_16x16.png
   :align: center

   vga2_16x16.py: 256 Character 16x16 Thin Font

|

.. figure:: _static/vga2_bold_16x16.png
   :align: center

   vga2_bold_16x16.py: 256 Character 16x16 Bold Font

|

16x32 Rom Fonts
"""""""""""""""

.. figure:: _static/vga1_16x32.png
   :align: center

   vga1_16x32.py: 128 Character 16x32 Thin Font

|

.. figure:: _static/vga1_bold_16x32.png
   :align: center

   vga1_bold_16x32.py: 128 Character 16x32 Bold Font

|

.. figure:: _static/vga2_16x32.png
   :align: center

   vga2_16x32.py: 256 Character 16x32 Thin Font

|

.. figure:: _static/vga2_bold_16x32.png
   :align: center

   vga2_bold_16x32.py: 256 Character 16x32 Bold Font



True Type fonts
---------------

The True-Type fonts can be converted to any size as long as the widest character is 256 pixels or less. They are written using the write method.


True-Type Font Conversion
^^^^^^^^^^^^^^^^^^^^^^^^^

The `utils` directory contains the `write_font_converter.py` program used to convert True-Type font into bitmap font modules. Use the -h option to see details of the available options.  The `write_font_converter.py` program uses font handling classes from Dan Bader blog post on using freetype http://dbader.org/blog/monochrome-font-rendering-with-freetype-and-python and the negative glyph.left fix from peterhinch's font conversion program https://github.com/peterhinch/micropython-font-to-py.

The utility requires the python freetype module.

Example use:

- ./write_font_converter.py NotoSans-Regular.ttf 32 -s "0123456789ABCEDF"
- ./write_font_converter.py Chango-Regular.ttf 16 -c 0x20-0x7f


.. literalinclude:: truetype.py
   :linenos:
   :language: python
   :caption: Sample converted TrueType font module.
