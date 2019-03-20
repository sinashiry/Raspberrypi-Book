import time
import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
lcd_rs        = 4
lcd_en        = 17
lcd_d4        = 27
lcd_d5        = 22
lcd_d6        = 24
lcd_d7        = 25
#lcd_backlight = 4

lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

lcd.message('Persian\nReference')
time.sleep(5.0)
lcd.clear()
lcd.message('BY')
time.sleep(5.0)
lcd.clear()
lcd.message('H.Alamshahi\nSina Shiri')
time.sleep(5.0)
lcd.clear()