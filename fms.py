from FMSBackend import *
from time import sleep
lcd_columns = 16
lcd_rows = 2
# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D21)
lcd_en = digitalio.DigitalInOut(board.D20)
lcd_d4 = digitalio.DigitalInOut(board.D26)
lcd_d5 = digitalio.DigitalInOut(board.D19)
lcd_d6 = digitalio.DigitalInOut(board.D13)
lcd_d7 = digitalio.DigitalInOut(board.D16)
# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                lcd_d7, lcd_columns, lcd_rows)
#lcd.clear()
while(True):
   l1 = "Scan Driver RFID\n"
   l2 = "Card ...... "
   lcd.clear()
   lcd.message = l1 + l2 
   id1, text = readRFID()
   lcd.clear()
   l1 = str(id1)
   lcd.message = l1  
   sleep(2)
   if(isDriverInDB(id1) == True):
      lcd.clear()
      lcd.message = "Driver Verified"
      sleep(2)
      lcd.clear()
      lcd.message = "Please Scan\nVehicle RFID"
      id2, text = readRFID()
      if(isVehicleInDB(id2) ==True):
         lcd.clear()
         lcd.message = "Vehicle Verified"
         sleep(2)
         lcd.clear()
         lcd.message = "Access \nGranted"
         unlockFuelPump()
         measureFuelOuttake()
       else:
         lcd.clear()
         lcd.message = "Vehicle Not\nfound"
         sleep(2)
   else:
      lcd.clear()
      lcd.message = "Driver Not\nfound"
      sleep(2)

