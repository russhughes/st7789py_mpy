# Conversion Utilites

## text_font_converter.py

Convert fonts from the font-bin directory of spacerace's https://github.com/spacerace/romfont VGA and BIOS rom font repo.

Reads all font-bin files from the specified `input` directory and writes python font modules for use with the text() method to the specified `output` directory. Optionally limiting the characters included to -first-char (-f) thru -last-char (-l).

```
usage: text_font_converter.py [-h] [-f FIRST_CHAR] [-l LAST_CHAR] input output

Convert fomfont.bin font files from `input` to python module(s) in `output` for use with the text() method.

positional arguments:
  input     file or directory containing binary font file(s).
  output    file or directory to contain python font file(s).

optional arguments:
  -h, --help                                show this help message and exit
  -f FIRST_CHAR, --first-char FIRST_CHAR    The first character code to include in the conversion (default: 0x20)
  -l LAST_CHAR, --last-char LAST_CHAR       The last character code to include in the conversion (default: 0x7F)
```

## write_font_converter.py

```
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
```

## image_converter.py

```
usage: image_converter.py [-h] image_file bits_per_pixel

Convert image file to python module for use with bitmap method.

positional arguments:
  image_file      Name of file containing image to convert
  bits_per_pixel  The number of bits to use per pixel (1..8)

optional arguments:
  -h, --help      show this help message and exit

```

## sprites_converter.py

Convert a sprite sheet image to python a module for use with indexed bitmap method.
Sprite sheet width and height should be a multiple of sprite width and height. There
should be no extra pixels between sprites. All sprites will share the same palette.

```
usage: sprites_converter [-h] image_file sprite_width sprite_height bits_per_pixel

Convert image file to python module for use with bitmap method.

positional arguments:
image_file      Name of file containing image to convert
sprite_width    width of sprites in pixels
sprite_height   Height of sprites in pixels
bits_per_pixel  The number of bits to use per pixel (1..8)

optional arguments:
-h, --help      show this help message and exit
```

## create_png_examples.py

```
usage: create_png_examples.py [-h] input output

Creates png samples of each text font file from the input directoryto the output directory.

positional arguments:
  input       input directory containing font-bin files
  output      output directory to create pngs

optional arguments:
  -h, --help  show this help message and exit
```
