"""
Module to create and update urban microclimate models, and perform urban microclimate simulations in sequence or parallel.

Delft University of Technology
Dr. Miguel Martin
"""
from abc import ABCMeta, abstractmethod
import numpy as np
from datetime import datetime, timedelta
from metpy.calc import dewpoint_from_relative_humidity, specific_humidity_from_dewpoint

import pandas as pd
import parseidf

from sciencespy.dom import *
from sciencespy.bem import *

class UrbanMicroclimateModel():
    """
    Class representing an urban microclimate model.

    Attributes:
        pool_bems: pool of models that are used to perform building energy simulations.
    """

    __metaclass__ = ABCMeta

    def __init__(self, pool_bems):
        """
        :param pool_bems: pool of models that are used to perform building energy simulations.
        """
        self.pool_bems = pool_bems

    @abstractmethod
    def run(self, start_date, end_date, dt = timedelta(hours = 1)):
        """
        Perform simulation of the urban microclimate model
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        pass

class StreetCanyonLoader():
    """
    Class to load a street canyon.

    Attributes:
        street_canyon_file: file containing details of the street canyon.
        bems_pool: pool of models that are used to perform building energy simulations.
    """
    __metaclass__ = ABCMeta

    def __init__(self, street_canyon_file, bems_pool):
        """
        :param street_canyon_file: file containing details of the street canyon.
        :param bems_pool: pool of models that are used to perform building energy simulations.
        """
        self.street_canyon_file = street_canyon_file
        self.bems_pool = bems_pool

    def load(self):
        """
        Load the street canyon from a file.
        :return: loaded street canyon.
        """
        street_canyon = StreetCanyon(self.get_street_canyon_name())
        street_canyon.atmosphere = self.get_street_canyon_atmosphere()
        street_canyon.pavements = self.get_street_canyon_pavements()
        street_canyon.surrounding_walls = self.get_street_canyon_surrounding_walls()
        street_canyon.waste_heat_sources = self.get_street_canyon_waste_heat_sources()
        street_canyon.traffic = self.get_street_canyon_traffic()
        street_canyon.vegetation = self.get_street_canyon_vegetation()
        street_canyon.weather_stations = self.get_street_canyon_weather_stations()
        return street_canyon

    @abstractmethod
    def get_street_canyon_name(self):
        """
        :return: name of the street canyon
        """
        pass

    @abstractmethod
    def get_street_canyon_atmosphere(self):
        """
        :return: atmoshperic layer of the street canyon
        """
        pass

    @abstractmethod
    def get_street_canyon_pavements(self):
        """
        :return: pavements of the street canyon
        """
        pass

    @abstractmethod
    def get_street_canyon_surrounding_walls(self):
        """
        :return: surrounding walls of the street canyon
        """
        pass

    @abstractmethod
    def get_street_canyon_waste_heat_sources(self):
        """
        :return: waste heat sources of the street canyon
        """
        pass

    @abstractmethod
    def get_street_canyon_traffic(self):
        """
        :return: traffic of the street canyon
        """
        pass

    @abstractmethod
    def get_street_canyon_vegetation(self):
        """
        :return: traffic of the street canyon
        """
        pass

    @abstractmethod
    def get_street_canyon_weather_stations(self):
        """
        :return: weather stations in the street canyon
        """
        pass


class UrbanCanopyModel(UrbanMicroclimateModel):
    """
    Class representing an urban canopy model.

    Attributes:
        street_canyon: street canyon being modelled by the urban canopy model.
        street_canyon_loader: loader of the street canyon.
    """
    __metaclass__ = ABCMeta

    def __init__(self, street_canyon_loader):
        """
        :param street_canyon_loader: loader of the street canyon.
        """
        UrbanMicroclimateModel.__init__(self, street_canyon_loader.bems_pool)
        self.street_canyon = None
        self.street_canyon_loader = street_canyon_loader

    def run(self, start_date, end_date, dt = timedelta(hours = 1)):
        """
        Perform simulation of the urban microclimate model
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        if self.street_canyon is None:
            self.street_canyon = self.street_canyon_loader.load()
        self.street_canyon = self.update_street_canyon(start_date, end_date, dt)

    @abstractmethod
    def update_street_canyon(self, start_date, end_date, dt):
        """
        Update the status of the street canyon.
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        :return: updated status of the street canyon from start_date to end_date at a rate of dt.
        """
        pass

class PavementTemperatureLoader():
    """
    Class to load the temperature of the pavement.

    Attributes:
        pavement_temperature_file: file containing the temperature of the pavement.
    """
    __metaclass__ = ABCMeta

    def __init__(self, pavement_temperature_file):
        """
        :param pavement_temperature_file: file containing the temperature of the pavement.
        """
        self.pavement_temperature_file = pavement_temperature_file

    def load(self):
        """
        Load the street canyon from a file.
        :return: loaded street canyon.
        """
        pavement_temperature = self.get_pavement_temperature()
        return pavement_temperature

    @abstractmethod
    def get_pavement_temperature(self):
        """
        :return: temperature of the pavement (in degree Celsius)
        """
        pass

class CSVPavementTemperatureLoader(PavementTemperatureLoader):
    """
    Class to load the temperature of the pavement from a .csv file.

    Attributes:
        pavement_temperature_file: file containing the temperature of the pavement.
    """
    __metaclass__ = ABCMeta

    def __init__(self, pavement_temperature_file):
        """
        :param pavement_temperature_file: file containing the temperature of the pavement.
        """
        PavementTemperatureLoader.__init__(self, pavement_temperature_file)

    def get_pavement_temperature(self):
        """
        :return: temperature of the pavement (in degree Celsius)
        """
        return pd.read_csv(self.pavement_temperature_file, index_col=0, parse_dates=True,
                           date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y %H:%M'))

class WeatherStationDataLoader():
    """
    Class to load data collected from a weather station.

    Attributes:
        weather_station_file: file containing data collected by a weather station.
    """
    __metaclass__ = ABCMeta

    def __init__(self, weather_station_file):
        """
        :param weather_station_file: file containing data collected by a weather station.
        """
        self.weather_station_file = weather_station_file

    def load(self):
        """
        Load the street canyon from a file.
        :return: loaded street canyon.
        """
        weather_data = self.get_weather_data()
        return weather_data

    @abstractmethod
    def get_weather_data(self):
        """
        :return: weather data collected by the station.
        """
        pass

class CSVWeatherStationDataLoader(WeatherStationDataLoader):
    """
    Class to load data collected from a weather station using the .csv format.

    Attributes:
        weather_station_file: .csv file containing data collected by a weather station.
    """

    def __init__(self, weather_station_file):
        """
        :param weather_station_file: .csv file containing data collected by a weather station.
        """
        WeatherStationDataLoader.__init__(self, weather_station_file)

    def get_weather_data(self):
        """
        :return: weather data collected by the station.
        """
        return pd.read_csv(self.weather_station_file, index_col=0, parse_dates=True,
                           date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y %H:%M'))

class AtmosphericDataLoader():
    """
    Class to load data at the atmospheric layer

    Attributes:
        atmospheric_file: file containing data at the atmospheric layer.
    """
    __metaclass__ = ABCMeta

    def __init__(self, atmospheric_file):
        """
        :param atmospheric_file: file containing data at the atmospheric layer.
        """
        self.atmospheric_file = atmospheric_file

    def load(self):
        """
        Load atmospheric data from a file.
        :return: loaded atmospheric data.
        """
        atmospheric_data = self.get_atmospheric_data()
        return atmospheric_data

    @abstractmethod
    def get_atmospheric_data(self):
        """
        :return: atmospheric data.
        """
        pass

class EPWAtmosphericDataLoader(AtmosphericDataLoader):
    """
    Class to load data at the atmospheric layer from .epw file.

    Attributes:
        atmospheric_file: file containing data at the atmospheric layer.
    """

    def __init__(self, atmospheric_file):
        """
        :param atmospheric_file: file containing data at the atmospheric layer.
        """
        AtmosphericDataLoader.__init__(self, atmospheric_file)

    def get_atmospheric_data(self):
        """
        :return: atmospheric data.
        """
        epw_weather_data = EPWDataLoader(self.atmospheric_file).load()
        temperature = epw_weather_data.outdoor_air_temperature
        relative_humidity = epw_weather_data.outdoor_air_relative_humidity
        pressure = epw_weather_data.outdoor_air_pressure
        dew_point = dewpoint_from_relative_humidity(temperature, relative_humidity)
        specific_humidity = specific_humidity_from_dewpoint(pressure, dew_point)
        d = {'Atmospheric Temperature': temperature, 'Atmospheric Humidity': specific_humidity}
        return pd.DataFrame(index=epw_weather_data.timestamps, data = d)


class IDFStreetCanyonLoader(StreetCanyonLoader):
    """
    Class to load a street canyon.

    Attributes:
        street_canyon_file: file containing details of the street canyon.
        bems_pool: pool of models that are used to perform building energy simulations.
        idf_objects: IDF objects containing information of the street canyon.
        atmospheric_data_dir: directory containing atmospheric data
        pavement_temperature_dir: directory containing measurements of the surface temperature.
        weather_data_dir: directory in which are stored weather data collected by several stations.
    """

    def __init__(self, street_canyon_file, bems_pool, atmosphere_dir = '.', pavement_temperature_dir = '.', weather_data_dir = '.'):
        """
        :param street_canyon_file: file containing details of the street canyon.
        :param bems_pool: pool of models that are used to perform building energy simulations.
        :param atmosphere_dir: directory containing measurements at the atmospheric layer.
        :param pavement_temperature_dir: directory containing measurements of the surface temperature.
        :param weather_data_dir: directory in which are stored weather data collected by several stations.
        """
        StreetCanyonLoader.__init__(self, street_canyon_file, bems_pool)
        with open(street_canyon_file, 'r') as f:
            self.idf_objects = parseidf.parse(f.read())
        self.pavement_temperature_dir = pavement_temperature_dir
        self.weather_data_dir = weather_data_dir
        self.atmosphere_dir = atmosphere_dir

    def get_street_canyon_name(self):
        """
        :return: name of the street canyon
        """
        return self.idf_objects['STREETCANYON'][0][1]

    def get_street_canyon_atmosphere(self):
        """
        :return: atmoshperic layer of the street canyon
        """
        atmosphere = Atmosphere()
        atmospheric_data = EPWAtmosphericDataLoader(self.atmosphere_dir + '\\' + self.idf_objects['STREETCANYON'][0][2] + '.epw').load()
        atmosphere.temperature = pd.Series(index=atmospheric_data.index, data=atmospheric_data['Atmospheric Temperature'])
        atmosphere.humidity = pd.Series(index=atmospheric_data.index, data=atmospheric_data['Atmospheric Humidity'])
        return atmosphere

    def get_street_canyon_pavements(self):
        """
        :return: pavements of the street canyon
        """
        pavements = []
        name_list_pavements = self.idf_objects['STREETCANYON'][0][4]
        for r in range(len(self.idf_objects['STREETCANYON:PAVEMENTS'])):
            if name_list_pavements == self.idf_objects['STREETCANYON:PAVEMENTS'][r][1]:
                number_pavements = len(self.idf_objects['STREETCANYON:PAVEMENTS'][r]) - 2
                for p in range(number_pavements):
                    pavement_name = self.idf_objects['STREETCANYON:PAVEMENTS'][r][p + 2]
                    for m in range(len(self.idf_objects['PAVEMENT'])):
                        if pavement_name == self.idf_objects['PAVEMENT'][m][1]:
                            pavement_points = []
                            count = 2
                            for n in range(int((len(self.idf_objects['PAVEMENT'][0]) - 2) / 2)):
                                pavement_points.append([float(self.idf_objects['PAVEMENT'][0][count]),
                                                        float(self.idf_objects['PAVEMENT'][0][count + 1]),
                                                        0.0])
                                count = count + 2
                            pavement = Surface(pavement_name, np.array(pavement_points))
                            pavement_temperature_loader = CSVPavementTemperatureLoader(self.pavement_temperature_dir + '//' + pavement_name + '.csv')
                            pavement_temperature = pavement_temperature_loader.load()
                            pavement.temperature = pd.Series(index=pavement_temperature.index, data=pavement_temperature['Surface Temperature'].values * units.degC)
                            pavements.append(pavement)
        return pavements

    def get_street_canyon_surrounding_walls(self):
        """
        :return: surrounding walls of the street canyon
        """
        surrounding_walls = []
        name_list_surrounding_walls = self.idf_objects['STREETCANYON'][0][3]
        for r in range(len(self.idf_objects['SURROUNDINGWALLS'])):
            if name_list_surrounding_walls == self.idf_objects['SURROUNDINGWALLS'][r][1]:
                number_list_surrounding_walls_per_building = len(self.idf_objects['SURROUNDINGWALLS'][r]) - 2
                for spb in range(number_list_surrounding_walls_per_building):
                    name_list_surrounding_walls_per_building =  self.idf_objects['SURROUNDINGWALLS'][r][spb + 2]
                    for sws in range(len(self.idf_objects['SURROUNDINGWALLS:BUILDING'])):
                        if name_list_surrounding_walls_per_building == self.idf_objects['SURROUNDINGWALLS:BUILDING'][sws][1]:
                            number_surrounding_walls = len(self.idf_objects['SURROUNDINGWALLS:BUILDING'][sws]) - 3
                            name_building = self.idf_objects['SURROUNDINGWALLS:BUILDING'][sws][2]
                            for sw in range(number_surrounding_walls):
                                name_surrounding_wall = self.idf_objects['SURROUNDINGWALLS:BUILDING'][sws][sw + 3].lower()
                                for bem in self.bems_pool.pool:
                                    if name_building == bem.building.name:
                                        surrounding_walls.append(bem.building.get_exterior_wall(name_surrounding_wall))
        return surrounding_walls

    def get_street_canyon_waste_heat_sources(self):
        """
        :param pool_bems: pool of models that are used to perform building energy simulations.
        :return: waste heat sources of the street canyon
        """
        return []

    def get_street_canyon_traffic(self):
        """
        :return: traffic of the street canyon
        """
        return []

    def get_street_canyon_vegetation(self):
        """
        :return: vegetation of the street canyon
        """
        return []

    def get_street_canyon_weather_stations(self):
        """
        :return: weather stations in the street canyon
        """
        weather_stations = []
        name_list_weather_stations = self.idf_objects['STREETCANYON'][0][9]
        for r in range(len(self.idf_objects['WEATHERSTATIONS'])):
            if name_list_weather_stations == self.idf_objects['WEATHERSTATIONS'][r][1]:
                number_weather_stations = len(self.idf_objects['WEATHERSTATIONS'][r]) - 2
                for n in range(number_weather_stations):
                    weather_station = WeatherStation(self.idf_objects['WEATHERSTATIONS'][r][n + 2])
                    weather_station_data = CSVWeatherStationDataLoader(self.weather_data_dir + '\\' + weather_station.name + '.csv').load()
                    weather_station.temperature = pd.Series(index=weather_station_data.index, data=weather_station_data['Outdoor Air Temperature'])
                    weather_station.humidity = pd.Series(index=weather_station_data.index, data=weather_station_data['Outdoor Air Relative Humidity'])
                    weather_station.pressure = pd.Series(index=weather_station_data.index, data=weather_station_data['Outdoor Air Pressure'])
                    weather_stations.append(weather_station)
        return weather_stations

class DataDrivenUrbanCanopyModel(UrbanCanopyModel):
    """
    Class representing a data driven urban canopy model.

    Attributes:
        street_canyon: street canyon being modelled by the urban canopy model.
        street_canyon_loader: loader of the street canyon.
    """
    __metaclass__ = ABCMeta

    def __init__(self, street_canyon_loader):
        """
        :param urban_microclimate_file: file containing details of the data driven urban canopy model.
        """
        UrbanCanopyModel.__init__(self, street_canyon_loader)

    def update_street_canyon(self, start_date, end_date, dt):
        """
        Update the status of the street canyon.
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        :return: updated status of the street canyon from start_date to end_date at a rate of dt.
        """
        pass


