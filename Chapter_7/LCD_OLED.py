import time
from datetime import datetime
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)
# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Load default font.
font = ImageFont.load_default()
# Write two lines of text.
padding = 2
top = padding
x = padding
disp.display()
while True:
	draw.text((x, top),    'RPi Persian Reference',  font=font, fill=255)
	draw.text((x, top+12), 'By: H.alamshahi &', font=font, fill=255)
	draw.text((x, top+24), '    S.Shiri', font=font, fill=255)
	now = datetime.now()
	draw.text((x, top+36), '  {:%d %B %Y}'.format(now),  font=font, fill=255)
	draw.text((x, top+48), '     {:%H:%M:%S}'.format(now),  font=font, fill=255)
        disp.image(image)
	disp.display()
	time.sleep(0.2)
	image = Image.new('1', (width, height))
	draw = ImageDraw.Draw(image)
