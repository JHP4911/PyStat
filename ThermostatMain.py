__author__ = 'matt'
import time
import threading
from FileManager import FileManager
import ThermostatConfiguration
from ThermostatService import ThermostatService
from ThermostatScheduler import ThermostatScheduler
from ThermostatWeb import ThermostatWeb
from TemperatureReader import TemperatureReader
from ThermostatWeather import ThermostatWeather

def main():

    # magic constants
    configurationFileName = "thermostat.conf"
    currentFileName = "current.set"
    scheduleFileName = "schedule.conf"

    # make the static utility classes
    fileManager = FileManager(configurationFileName, currentFileName, scheduleFileName)
    configuration = fileManager.read_configuration()
    temperatureReader = TemperatureReader()
    weather = ThermostatWeather(configuration.weatherAPIKey, configuration.weatherurl,
                                configuration.latlong, configuration.weatherFlags)

    if configuration is None:
        print("Configuration file could not be read.")
        exit(1)

    if "-1" == configuration.heatPin \
            or "-1" == configuration.acPin \
            or "-1" == configuration.fanPin \
            or configuration.heatPin == configuration.acPin \
            or configuration.heatPin == configuration.fanPin \
            or configuration.acPin == configuration.fanPin:
        print("The pin settings provided are invalid:")
        print("\tHeat pin: " + str(configuration.heatPin))
        print("\tAC pin: " + str(configuration.acPin))
        print("\tFan pin: " + str(configuration.fanPin))
        exit(2)

    service = ThermostatService(0, "service", configuration, fileManager,
                                temperatureReader)
    service.start()

    scheduler = ThermostatScheduler(1, "scheduler", configuration, fileManager,
                                    temperatureReader)
    scheduler.start()

    web = ThermostatWeb(2, "web", configuration, fileManager,
                        temperatureReader, weather)
    web.start()

    while True:
        print("Polling threads")
        if not service.is_alive():
            print("PANIC SERVICE IS DEAD")
        if not scheduler.is_alive():
            print("PANIC SCHEDULER IS DEAD")
        if not web.is_alive():
            print("PANIC WEB IS DEAD")

        time.sleep(30)

main()