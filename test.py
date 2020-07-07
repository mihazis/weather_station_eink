"""
	Example for 4.2 inch black & white Waveshare E-ink screen
	Run on ESP32
"""

import epaper2in7b
from machine import Pin, SPI

# SPIV on ESP32
sck = Pin(18)
miso = Pin(19)
mosi = Pin(23)										
dc = Pin(17)
cs = Pin(5)
rst = Pin(16)
busy = Pin(4)
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=sck, miso=miso, mosi=mosi)
# write hello world with black bg and white text
from image_dark import hello_world_dark
from image_light import hello_world_light
print('Image dark')

e = epaper2in7b.EPD(spi, cs, dc, rst, busy)
e.init()


w = 400
h = 300
x = 0
y = 0

import framebuf
buf = bytearray(w * h // 8)
fb = framebuf.FrameBuffer(buf, w, h, framebuf.MONO_HLSB)
black = 0
white = 1
fb.fill(white)
print('Image dark')