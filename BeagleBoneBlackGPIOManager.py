__author__ = 'matt'

from GPIOManager import GPIOManager
import Adafruit_BBIO.GPIO as bbbGPIO


class BeagleBoneBlackGPIOManager(GPIOManager):
    def __init__(self, configuration):
        GPIOManager.__init__(self, configuration)

    def turn_off_fan(self):
        try:
            bbbGPIO.output(self.configuration.fanPin, bbbGPIO.LOW)
        except:
            bbbGPIO.setup(self.configuration.fanPin, bbbGPIO.OUT)
            bbbGPIO.output(self.configuration.fanPin, bbbGPIO.LOW)

    def turn_on_fan(self):
        try:
            bbbGPIO.output(self.configuration.fanPin, bbbGPIO.HIGH)
        except:
            bbbGPIO.setup(self.configuration.fanPin, bbbGPIO.OUT)
            bbbGPIO.output(self.configuration.fanPin, bbbGPIO.HIGH)

    def turn_off_ac(self):
        try:
            bbbGPIO.output(self.configuration.acPin, bbbGPIO.LOW)
        except:
            bbbGPIO.setup(self.configuration.acPin, bbbGPIO.OUT)
            bbbGPIO.output(self.configuration.acPin, bbbGPIO.LOW)

    def turn_on_ac(self):
        try:
            bbbGPIO.output(self.configuration.acPin, bbbGPIO.HIGH)
        except:
            bbbGPIO.setup(self.configuration.acPin, bbbGPIO.OUT)
            bbbGPIO.output(self.configuration.acPin, bbbGPIO.HIGH)

    def turn_off_heat(self):
        try:
            bbbGPIO.output(self.configuration.heatPin, bbbGPIO.LOW)
        except:
            bbbGPIO.setup(self.configuration.heatPin, bbbGPIO.OUT)
            bbbGPIO.output(self.configuration.heatPin, bbbGPIO.LOW)

    def turn_on_heat(self):
        try:
            bbbGPIO.output(self.configuration.heatPin, bbbGPIO.HIGH)
        except:
            bbbGPIO.setup(self.configuration.heatPin, bbbGPIO.OUT)
            bbbGPIO.output(self.configuration.heatPin, bbbGPIO.HIGH)
