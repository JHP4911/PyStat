__author__ = 'matt'

#import RPi.GPIO as rpiGPIO
#import Adafruit_BBIO.GPIO as bbbGPIO

class GPIOManager():
    def __init__(self, configuration):
        self.configuration = configuration

    def turn_off_fan(self):
        pass

    def turn_on_fan(self):
        pass

    def turn_off_ac(self):
        pass

    def turn_on_ac(self):
        pass

    def turn_off_heat(self):
        pass

    def turn_on_heat(self):
        pass
'''
class RaspberryPiManager(GPIOManager):
    def __init__(self, configuration):
        GPIOManager.__init__(self, configuration)
        rpiGPIO.setmode(rpiGPIO.BCM)

    def turn_off_fan(self):
        pin = int(self.configuration.fanPin)
        try:
            rpiGPIO.output(pin, False)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, False)

    def turn_on_fan(self):
        pin = int(self.configuration.fanPin)
        try:
            rpiGPIO.output(pin, True)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, True)

    def turn_off_ac(self):
        pin = int(self.configuration.acPin)
        try:
            rpiGPIO.output(pin, False)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, False)

    def turn_on_ac(self):
        pin = int(self.configuration.acPin)
        try:
            rpiGPIO.output(pin, True)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, True)

    def turn_off_heat(self):
        pin = int(self.configuration.heatPin)
        try:
            rpiGPIO.output(pin, False)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, False)

    def turn_on_heat(self):
        pin = int(self.configuration.heatPin)
        try:
            rpiGPIO.output(pin, True)
        except:
            rpiGPIO.setup(pin, rpiGPIO.OUT)
            rpiGPIO.output(pin, True)

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
'''

class TestGPIOManager(GPIOManager):
    def __init__(self, configuration):
        GPIOManager.__init__(self, configuration)

    def turn_off_fan(self):
        # turn off the fan
        print("turn fan pin off")

    def turn_on_fan(self):
        # turn on the fan
        print("turn fan pin on")

    def turn_off_ac(self):
        # turn off the ac
        print("turn ac pin off")

    def turn_on_ac(self):
        # turn on the ac
        print("turn ac pin on")

    def turn_off_heat(self):
        # turn off the heat
        print("turn heat pin off")

    def turn_on_heat(self):
        # turn on the heat
        print("turn heat pin on")
