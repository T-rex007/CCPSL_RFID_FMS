# Software SPI configuration:

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def readADCValue(): 
    # create the spi bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    
    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D)
    
    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)
    
    # create an analog input channel on pin 0
    chan = AnalogIn(mcp, MCP.P0)
    
    print('Raw ADC Value: ', chan.value)
    print('ADC Voltage: ' + str(chan.voltage) + 'V')
    GPIO.cleanip()

def readRFID():
    reader = SimpleMFRC522()
    try:
            id, text = reader.read()
            print(id)
            print(text)
    finally:
            GPIO.cleanup()
    
if __name__=="__main__":
    readADCValue()
    readRFID()

