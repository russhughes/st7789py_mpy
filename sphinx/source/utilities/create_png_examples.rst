.. _create_png_examples:

create_png_examples.py
----------------------
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

