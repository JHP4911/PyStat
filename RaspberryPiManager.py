__author__ = 'matt'

import RPi.GPIO as rpiGPIO
from GPIOManager import GPIOManager

# Due to the annoying fact that on HIGH, relay is off, vice versa.
# Please comment out these two lines if you are testing with LEDs,
# Otherwise you'll get reverse light signal.
RELAY_ON = False 
RELAY_OFF = True

class RaspberryPiManager(GPIOManager):
    def __init__(self, configuration):
        GPIOManager.__init__(self, configuration)
        rpiGPIO.setmode(rpiGPIO.BCM)

    def turn_off_fan(self):
        pin = int(self.configuration.fanPin)
        try:
            rpiGPIO.output(pin, RELAY_OFF)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, RELAY_OFF) 

    def turn_on_fan(self):
        pin = int(self.configuration.fanPin)
        try:
            rpiGPIO.output(pin, RELAY_ON)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, RELAY_ON)

    def turn_off_ac(self):
        pin = int(self.configuration.acPin)
        try:
            rpiGPIO.output(pin, RELAY_OFF)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, RELAY_OFF)

    def turn_on_ac(self):
        pin = int(self.configuration.acPin)
        try:
            rpiGPIO.output(pin, RELAY_ON)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, RELAY_ON)

    def turn_off_heat(self):
        pin = int(self.configuration.heatPin)
        try:
            rpiGPIO.output(pin, RELAY_OFF)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, RELAY_OFF)

    def turn_on_heat(self):
        pin = int(self.configuration.heatPin)
        try:
            rpiGPIO.output(pin, RELAY_ON)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, RELAY_ON)
