"""converted from vga_8x8.bin """

# font width
WIDTH = 8

# font height
HEIGHT = 8

# first character in front
FIRST = 0x20

# last character in font
LAST = 0x7f

# bitmap of each character from FIRST to LAST
_FONT =\
b'\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x18\x3c\x3c\x18\x18\x00\x18\x00'\
b'\x66\x66\x24\x00\x00\x00\x00\x00'\

... many more lines of data...

b'\x70\x18\x18\x0e\x18\x18\x70\x00'\
b'\x76\xdc\x00\x00\x00\x00\x00\x00'\
b'\x00\x10\x38\x6c\xc6\xc6\xfe\x00'\

FONT = memoryview(_FONT)
