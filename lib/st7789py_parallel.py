# Extended Class to use TFT ST7789 in parallel bus
#Example of use:

# import st7789py_parallel
# s=st7789py_parallel.ST7789_PARALLEL(320,240,0,None,None,4,22,5,12)
# s.fill(0xff)


from micropython import const
from utime import sleep_ms, sleep_us
from machine import Pin

## Pins (wiring) example and description
#ST7789        STM32F407VGT6
#LCD_RST <---> 3.3V            #LCD reset control pin, active low, used to force a hardware reset of the board, if unused need be plug on 3.3V 
#LCD_CS  <---> GND             #LCD chip select control pin, active low, if unused only one LCD can be used, plug on GND
#LCD_RS  <---> PD22            #LCD register command / data selection control pin, comand active low, data active high
#LCD_WR  <---> PD4             #LCD write control pin, active low
#LCD_RD  <---> PD5             #LCD read control pin, active low, if unused plug on 3.3V
#GND     <---> GND
#5V      <---> 5V

#LCD_D2  <---> pin-14
#LCD_D3  <---> pin-15
#LCD_D4  <---> pin-16
#LCD_D5  <---> pin-17
#LCD_D6  <---> pin-18
#LCD_D7  <---> pin-19
#LCD_D0  <---> pin-12
#LCD_D1  <---> pin-13

## DEFINE PINS CONST
_LCD_RST       = const(None)      #LCD reset control pin, active low
_LCD_CS        = const(None)      #LCD chip select control pin, active low
_LCD_RS        = const(4)         #LCD register command / data selection control pin, comand active low, data active high
_LCD_WR        = const(5)         #LCD write control pin, active low
_LCD_RD        = const(None)      #LCD read control pin, active low

_LCD_D0        = const(12)
_LCD_D1        = const(_LCD_D0 + 1)
_LCD_D2        = const(_LCD_D0 + 2)
_LCD_D3        = const(_LCD_D0 + 3)
_LCD_D4        = const(_LCD_D0 + 4)
_LCD_D5        = const(_LCD_D0 + 5)
_LCD_D6        = const(_LCD_D0 + 6)
_LCD_D7        = const(_LCD_D0 + 7)

## ESP32 GPIO REGISTERS
_ESP32_GPIO_OUT_REG       = const(0x3FF44004)  # GPIO0-31 output value. (R/W), 32 bits from rigth to left ref pins numbers from 0 to 31
_ESP32_GPIO_OUT_W1TS_REG  = const(0x3FF44008)  # GPIO0-31 output set register. For every bit that is 1 in the value written here, the corresponding bit in GPIO_OUT_REG will be set. (WO)
_ESP32_GPIO_OUT_W1TC_REG  = const(0x3FF4400C)  # GPIO0-31 output clear register. For every bit that is 1 in the value written here, the corresponding bit in GPIO_OUT_REG will be cleared. (WO)

_ESP32_GPIO_OUT1_REG       = const(0x3FF44010)  # GPIO32-39 output value. (R/W), 32 bits from rigth to left ref pins numbers from 32 to 39
_ESP32_GPIO_OUT1_W1TS_REG  = const(0x3FF44014)  # GPIO32-39 output set register. For every bit that is 1 in the value written here, the corresponding bit in GPIO_OUT_REG will be set. (WO)
_ESP32_GPIO_OUT1_W1TC_REG  = const(0x3FF44018)  # GPIO32-39 output clear register. For every bit that is 1 in the value written here, the corresponding bit in GPIO_OUT_REG will be cleared. (WO)

_ESP32_GPIO_IN_REG        = const(0x3FF4403C)  #GPIO 0-31 input register (RO)
_ESP32_GPIO_IN1_REG       = const(0x3FF44040)  #GPIO 32-39 input register (RO)

from st7789py import *

_ENCODE_PIXEL = const(">H")
_ENCODE_POS = const(">HH")
_DECODE_PIXEL = const(">BBB")

def _encode_pos(x, y):
    """Encode a postion into bytes."""
    return struct.pack(_ENCODE_POS, x, y)


def _encode_pixel(color):
    """Encode a pixel color into bytes."""
    return struct.pack(_ENCODE_PIXEL, color)



class ST7789_PARALLEL(ST7789):
    def __init__(self, width:(int) = 320, height:(int) = 240, rotation=0,
                       rst_pin:(int,None) = _LCD_RST, #             LCD reset control pin
                       cs_pin:(int,None)  = _LCD_CS,  #             LCD chip select control pin
                       rs_pin:(int,None)  = _LCD_RS,  #**Required** LCD register command / data selection control pin,
                       wr_pin:(int,None)  = _LCD_WR,  #**Required** LCD write control pin, active low
                       rd_pin:(int,None)  = _LCD_RD,  #             LCD read control pin, active low
                       d0_pin:(int,None)  = _LCD_D0   #**Required** LCD D0 pin, all otherpins will be pick seguentially after this.
                       ):
        if height != 240 or width not in [320, 240, 135]:
            raise ValueError("Unsupported display. 320x240, 240x240 and 135x240 are supported.")
        if rs_pin is None:
            raise ValueError("rs pin (data/command) is required.")
        if d0_pin is None or (d0_pin + 8) > 31 :
            raise ValueError("d0_pin is required, need to be continuos and bellow 23, the rest of data pins will be assign seguentially, ex, d0_pin = 12, d1_pin=13, ... ")
        
        for x in (rst_pin, cs_pin, rs_pin, wr_pin, rd_pin, d0_pin):
            if x != None and ((x<0) or (x>44)) :
                raise ValueError("Pins numbers need to between 0 and 44")
        
        
        self.rst_pin_mask = self.cs_pin_mask = self.rs_pin_mask = (_ESP32_GPIO_OUT_REG, 0b0)
        self.wr_pin_mask = self.rd_pin_mask = self.d_pin_mask = self.rst_pin_mask
    
        self.rst_pin = self.reset = rst_pin 
        if rst_pin != None :
            self.rst_pin = self.reset = Pin(rst_pin, Pin.OUT, value=1)
            if rst_pin < 32 :
                self.rst_pin_mask = (_ESP32_GPIO_OUT_REG, 1 << rst_pin)
            else :
                self.rst_pin_mask = (_ESP32_GPIO_OUT1_REG, 1 << rst_pin-32)

        self.cs_pin = self.cs = cs_pin
        if cs_pin != None :
            self.cs_pin = self.cs = Pin(cs_pin,Pin.OUT, value=1)
            if cs_pin < 32 :
                self.cs_pin_mask = (_ESP32_GPIO_OUT_REG, 1 << cs_pin)
            else :
                self.cs_pin_mask = (_ESP32_GPIO_OUT1_REG, 1 << cs_pin-32)
        
        self.rs_pin = self.dc = rs_pin
        if rs_pin != None :
            self.rs_pin = self.dc = Pin(rs_pin, Pin.OUT, value=0)
            if rs_pin < 32 :
                self.rs_pin_mask = (_ESP32_GPIO_OUT_REG, 1 << rs_pin)
            else :
                self.rs_pin_mask = (_ESP32_GPIO_OUT1_REG, 1 << rs_pin-32)
        
        self.wr_pin = wr_pin
        if wr_pin != None :
            self.wr_pin = Pin(wr_pin, Pin.OUT, value=1)
            if wr_pin < 32 :
                self.wr_pin_mask = (_ESP32_GPIO_OUT_REG, 1 << wr_pin)
            else :
                self.wr_pin_mask = (_ESP32_GPIO_OUT1_REG, 1 << wr_pin-32)
        
        self.rd_pin = rd_pin
        if rd_pin != None :
            self.rd_pin = Pin(rd_pin, Pin.OUT, value=1)
            if rd_pin < 32 :
                self.rd_pin_mask = (_ESP32_GPIO_OUT_REG, 1 << rd_pin)
            else :
                self.rd_pin_mask = (_ESP32_GPIO_OUT1_REG, 1 << rd_pin-32)
        
        self.d_pin = []
        for x in range(0, 8) :
            self.d_pin.append(Pin(d0_pin + x, Pin.OUT, value=0))
        self.d_pin_mask = (_ESP32_GPIO_OUT_REG, 0b11111111 << d0_pin)
        self.d0_pin = d0_pin

        self._display_width = self.width = width
        self._display_height = self.height = height
        self.xstart = 0
        self.ystart = 0
        
        self.backlight = None
        self._rotation = rotation % 4

        self.hard_reset()
        self.soft_reset()
        self.sleep_mode(False)

        self._set_color_mode(COLOR_MODE_65K | COLOR_MODE_16BIT)
        time.sleep_ms(50)
        self.rotation(self._rotation)
        self.inversion_mode(False)
        time.sleep_ms(10)
        self._write(ST7789_NORON)
        time.sleep_ms(10)
        self.fill(0)
        self._write(ST7789_DISPON)
        time.sleep_ms(500)

    @micropython.viper
    def _write_v(self, data: ptr8, size:int, repeat:int):
        gpio_data   = ptr32(self.d_pin_mask[0])
        gpio_wr     = ptr32(self.wr_pin_mask[0])
        wr_pin_mask = int(self.wr_pin_mask[1])
        d_pin_mask  = int(self.d_pin_mask[1])
        d0_pin      = int(self.d0_pin)
        for _ in range(0,repeat):
            for x in range(0,size):
                gpio_data[2] = d_pin_mask
                gpio_data[1] = int(data[x] << d0_pin)
                gpio_wr[2] = wr_pin_mask
                gpio_wr[1] = wr_pin_mask

    @micropython.native
    def _write(self, command=None, data=None, repeat=1):
        """ParallelSPI write to the device: commands and data."""
        if self.cs:
            self.cs.off()

        if command is not None:
            self.dc.off()
            if command is not None:
                command=bytearray([command])
                self._write_v(command,len(command), repeat)
        if data is not None:
            self.dc.on()
            if data is not None:
                self._write_v(data,len(data), repeat)
            if self.cs:
                self.cs.on()
        
    def fill_rect(self, x, y, width, height, color):
        """
        Draw a rectangle at the given location, size and filled with color.

        Args:
            x (int): Top left corner x coordinate
            y (int): Top left corner y coordinate
            width (int): Width in pixels
            height (int): Height in pixels
            color (int): 565 encoded color
        """
        self._set_window(x, y, x + width - 1, y + height - 1)
        pixel = _encode_pixel(color)
        
        self._write(None,pixel,width * height)

