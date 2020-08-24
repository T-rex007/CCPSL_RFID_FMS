
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import RPi.GPIO as GPIO
from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime
from mfrc522 import SimpleMFRC522
from pandas import DataFrame, read_csv
from gpiozero import MCP3008


def isDriverInDB(driver_id):
    return True
def isVehicleInDB(vehicle_id):
    return True
def addDriverToDB():
    return 0
def updateDriverList(report):
    """
    Args:
        Report: Dictionary with the pre-specified format Driver_data.csv
            (Same header names) 
    """
    df_new = DataFrame(report)
    df1 = read_csv("logs/Driver_data.csv",index_col =  False)
    df = df1.append(df_new, ignore_index = True
          )
    df.to_csv("logs/Driver_data.csv", index = False)
    
def updateVehicleList(report):
    """
    Args:
        Report: Dictionary with the pre-specified format of Vehicle_data.csv
            (Same header names) 
    """
    df_new = DataFrame(report)
    df1 = read_csv("logs/Vehicle_data.csv",index_col =  False)
    df = df1.append(df_new, ignore_index = True
          )
    df.to_csv("logs/Vehicle_data.csv", index = False)

def displayOnLCD(line1, line2):
    GPIO.cleanup()
     
    # Modify this if you have a different sized character LCD
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
    # wipe LCD screen before we start
    lcd.clear()    
    # combine both lines into one update to the display
    lcd.message = line1 + line2
    sleep(2)
    GPIO.cleanup()

def readADCValue(): 
    # Assign Pins for software spi
    clk = 18
    miso = 23
    mosi = 24
    cs = 12
    adc = MCP3008(channel = 0, clock_pin = clk, mosi_pin = mosi, miso_pin = miso, select_pin = cs)
    GPIO.cleanup()
    return adc.voltage

def readRFID():
    reader = SimpleMFRC522()
    try:
            id, text = reader.read()
            print(id)
            print(text)
    finally:
            #GPIO.cleanup()
            return (id,text)
