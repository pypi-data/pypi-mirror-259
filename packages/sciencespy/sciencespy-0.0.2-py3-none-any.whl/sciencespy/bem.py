"""
Module to create and update building energy models, and perform building energy simulation in sequence or parallel.

Delft University of Technology
Dr. Miguel Martin
"""

from abc import ABCMeta, abstractmethod
import os

import numpy as np
import opyplus as op
import shutil
import subprocess
import datetime

from pint import UnitRegistry
ureg = UnitRegistry()
ureg.default_format = '.3f'
ureg.define('percent = 0.01*count = %')
Q_ = ureg.Quantity

class WeatherData():
    """
    Class containing weather data.

    """
    __metaclass__ = ABCMeta
    @abstractmethod
    def get_latitude(self):
        """
        :return: latitude weather data were collected
        """
        pass
    @abstractmethod
    def set_latitude(self, new_latitude):
        """
        :param new_latitude: latitude weather data were collected
        """
        pass
    @abstractmethod
    def get_longitude(self):
        """
        :return: longitude weather data were collected
        """
        pass
    @abstractmethod
    def set_longitude(self, new_longitude):
        """
        :param new_longitude: longitude weather data were collected
        """
        pass
    @abstractmethod
    def get_timestamps(self):
        """
        :return: timestamps at which weather data were collected
        """
        pass
    @abstractmethod
    def get_outdoor_air_temperature(self):
        """
        :return: the outdoor air temperature (in ^oC)
        """
        pass
    @abstractmethod
    def set_outdoor_air_temperature(self, new_timestamps, new_outdoor_air_temperature):
        """
        :param new_timestamps: timestamps at which the new outdoor air temperature was measured or assessed.
        :param new_outdoor_air_temperature: new values for the outdoor air temperature (in ^oC)
        """
        pass
    def get_outdoor_air_relative_humidity(self):
        """
        :return: the outdoor air relative humidity (in %)
        """
        pass
    @abstractmethod
    def set_outdoor_air_relative_humidity(self, new_timestamps, new_outdoor_air_relative_humidity):
        """
        :param new_timestamps: timestamps at which the new outdoor air relative humidity was measured or assessed.
        :param new_outdoor_air_relative_humidity: new values for the outdoor air relative humidity (in %)
        """
        pass
    @abstractmethod
    def save(self, file_name, out_dir='.'):
        """
        Save weather data.
        :param file_name: file name where weather data must be saved
        :param out_dir: output directory where weather data must be saved
        """
        pass

class EnergyPlusWeatherData(WeatherData):
    """
    Class representing EnergyPlus weather data.

    Attributes:
        raw_epw_data: raw epw data.
    """

    raw_epw_data = []

    @staticmethod
    def load(epw_weather_file, weather_data_year = datetime.date.today().year):
        """
        Load EnergyPlus Weather (EPW) data
        :param epw_weather_file: EPW file containing weather data
        :param weather_data_year: year at which weather data were measured
        :return: EPW data
        """
        weather_data = EnergyPlusWeatherData()
        weather_data.raw_epw_data = op.WeatherData.load(epw_weather_file)
        weather_data.raw_epw_data.create_datetime_instants(start_year = weather_data_year)
        return weather_data
    def get_latitude(self):
        """
        :return: latitude weather data were collected
        """
        return float(self.raw_epw_data._headers['latitude'])
    def set_latitude(self, new_latitude):
        """
        :param new_latitude: latitude weather data were collected
        """
        self.raw_epw_data._headers['latitude'] = str(new_latitude)
    def get_longitude(self):
        """
        :return: longitude weather data were collected
        """
        return float(self.raw_epw_data._headers['longitude'])
    def set_longitude(self, new_longitude):
        """
        :param new_longitude: longitude weather data were collected
        """
        self.raw_epw_data._headers['longitude'] = str(new_longitude)
    def get_timestamps(self):
        """
        :return: timestamps at which weather data were collected
        """
        return self.raw_epw_data.get_weather_series().axes[0]

    def get_outdoor_air_temperature(self):
        """
        :return: the outdoor air temperature (in ^oC)
        """
        return Q_(np.asarray(self.raw_epw_data.get_weather_series()['drybulb']), 'degC')

    def set_outdoor_air_temperature(self, new_timestamps, new_outdoor_air_temperature):
        """
        :param new_timestamps: timestamps at which the new outdoor air temperature was measured or assessed.
        :param new_outdoor_air_temperature: new values for the outdoor air temperature (in ^oC)
        """
        ctimestamps = [t.timestamp() for t in self.get_timestamps()]
        ntimestamps = [t.timestamp() for t in new_timestamps]
        current_outdoor_temperature = np.interp(ctimestamps, ntimestamps, new_outdoor_air_temperature)
        cdf = self.raw_epw_data.get_weather_series()
        cdf['drybulb'] = current_outdoor_temperature
        self.raw_epw_data.set_weather_series(cdf)
    def get_outdoor_air_relative_humidity(self):
        """
        :return: the outdoor air relative humidity (in %)
        """
        return Q_(np.asarray(self.raw_epw_data.get_weather_series()['relhum']), 'percent')
    @abstractmethod
    def set_outdoor_air_relative_humidity(self, new_timestamps, new_outdoor_air_relative_humidity):
        """
        :param new_timestamps: timestamps at which the new outdoor air relative humidity was measured or assessed.
        :param new_outdoor_air_relative_humidity: new values for the outdoor air relative humidity (in %)
        """
        ctimestamps = [t.timestamp() for t in self.get_timestamps()]
        ntimestamps = [t.timestamp() for t in new_timestamps]
        current_outdoor_temperature = np.interp(ctimestamps, ntimestamps, new_outdoor_air_relative_humidity)
        cdf = self.raw_epw_data.get_weather_series()
        cdf['relhum'] = current_outdoor_temperature
        self.raw_epw_data.set_weather_series(cdf)
    def save(self, file_name, out_dir='.'):
        """
        Save weather data.
        :param file_name: file name where weather data must be saved
        :param out_dir: output directory where weather data must be saved
        """
        self.raw_epw_data.save(os.path.join(out_dir, file_name))

class BuildingEnergyModel():
    """
    Class representing a building energy model.

    Attributes:
        outdoor_conditions: weather conditions to be considered as boundary conditions of the building energy model.
    """
    __metaclass__ = ABCMeta

    outdoor_conditions = []

    def add_building_data(self, building, adding_procedures):
        """
        Add building data into the building energy model.
        :param buidling: building data to be added in the building energy model
        :param adding_procedures: list of procedures to add building data
        :return: building energy model with added data.
        """
        for ap in adding_procedures:
            self = ap.add(self, building)
        return self

    @abstractmethod
    def run(self):
        """
        Perform simulation using the building energy model.
        """
        pass

class EnergyPlusModel(BuildingEnergyModel):
    """
    Class representing an EnergyPlus model

    Attributes:
        energyplus_objects: element containing all EnergyPlus objects stored in an IDF file

        output_directory: directory in which outputs of EnergyPlus simulations must be stored
        must_expand_objects: if EnergyPlus objects must be expanded
    """

    energyplus_objects = []
    output_directory = '.'
    must_expand_objects = True
    @staticmethod
    def load(self, idf_file):
        """
        Loading an EnergyPlus model from IDF file.
        :param idf_file: idf file containing parameters of the EnergyPlus model
        :return: the EnergyPlus model
        """
        bem = EnergyPlusModel()
        bem.energyplus_objects = op.Epm.load(idf_file)
        return bem
    @staticmethod
    def load_from_template(building, template_file):
        """
        Loading an EnergyPlus model from template file.
        :param building: building data that must be included in the EnergyPlus model
        :param template_file: the template file with initial parameters of the EnergyPlus model
        :return: the EnergyPlus model
        """
        bem = EnergyPlusModel.load(template_file)
        adding_procedures = [AddLocationEnergyPlusModel(), AddZonesEnergyPlusModel(),
                             AddGroundFloorSurfaceEnergyPlusModel(), AddRoofSurfacesEnergyPlusModel(),
                             AddExteriorWallSurfacesEnergyPlusModel(), AddHeatingLoadEnergyPlusModel(),
                             AddCoolingLoadEnergyPlusModel()]
        return bem.add_building_data(building, adding_procedures)

    @abstractmethod
    def run(self):
        """
        Perform simulation using the EnergyPlus model.
        """
        self.energyplus_objects.save('in.idf')
        in_idf = 'in.idf'
        if self.must_expand_objects:
            shutil.copy(os.getenv('ENERGYPLUS') + '\\ExpandObjects.exe', '.')
            shutil.copy(os.getenv('ENERGYPLUS') + '\\Energy+.idd', '.')
            subprocess.call('ExpandObjects')
            in_idf = "expanded.idf"
        self.energyplus_objects = op.Epm.load(in_idf)
        # TODO: implement
        #s = op.simulate(self.energyplus_objects, weather_data, output_dir)
        #eso = s.get_out_eso()
        #return eso.get_data()


class AddBuildingData():
    """
    Class representing a procedure to add building data into a building energy model.

    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, bem, building):
        """
        Add building data into a building energy model
        :param bem: the building energy model before adding building data
        :param building: the building data to add
        :return: the building energy model after adding building data
        """
        pass


class AddLocationEnergyPlusModel(AddBuildingData):
    """
    Class add the location in the EnergyPlus model
    """

    def add(self, bem, building):
        """
        Add the location into an EnergyPlus model
        :param bem: the EnergyPlus model before adding the location
        :param building: the building data containing the location
        :return: the building energy model after adding the location
        """
        utc = datetime.datetime.now(building.location.timezone).utcoffset().total_seconds() / 3600

        bem.energyplus_objects.Site_Location.add(
            name = building.location.name,
            latitude = round(building.location.latitude.m, 3),
            longitude = round(building.location.longitude.m, 3),
            time_zone = round(utc, 1),
            elevation = round(building.location.altitude.m, 3)
        )
        return bem

class AddZonesEnergyPlusModel(AddBuildingData):
    """
    Class add zones in the EnergyPlus model
    """

    def add(self, bem, building):
        """
        Add zones into an EnergyPlus model
        :param bem: the EnergyPlus model before adding zones
        :param building: the building data containing zones
        :return: the building energy model after adding zones
        """
        if len(building.zones) == 1:
            zone = bem.energyplus_objects.Zone.one()
            zone.floor_area = round(building.zones[0].get_area().m, 3)
            zone.volume = round(building.zones[0].get_volume().m, 3)
        else:
            #TODO: implement
            pass
        return bem

class AddSurfacesEnergyPlusModel(AddBuildingData):
    """
    Class add surfaces in the EnergyPlus model
    """
    __metaclass__ = ABCMeta

    def update(self, bem, building):
        """
        Add surfaces into an EnergyPlus model
        :param bem: the EnergyPlus model before adding surfaces
        :param building: the building data containing surfaces
        :return: the building energy model after adding surfaces
        """
        for z in building.zones:
            surfaces = self.get_surfaces(z)
            for s in surfaces:
                buidling_surface_detailed = self.get_buidling_surface_detailed(bem, z, s)
                for p in s.points:
                    buidling_surface_detailed.add_fields(p.x, p.y, p.z)
        return bem

    @abstractmethod
    def get_surfaces(self, zone):
        """
        :param zone: zone in which the surface is located
        :return: surfaces to be added in the EnergyPlus file
        """
        pass

    @abstractmethod
    def get_buidling_surface_detailed(self, bem, zone, surface):
        """
        :param bem: EnergyPlus model
        :param zone: zone in which the surface is located
        :param surface: surface to be added in the EnergyPlus model
        :return: detailed of the surface
        """
        pass


class AddGroundFloorSurfaceEnergyPlusModel(AddSurfacesEnergyPlusModel):
    """
    Class add surfaces in the EnergyPlus model
    """
    def get_surfaces(self, zone):
        """
        :param zone: zone in which the surface is located
        :return: surfaces to be added in the EnergyPlus file
        """
        if not zone.ground_floor_surface is None:
            return [zone.ground_floor_surface]
        else:
            return []

    def get_buidling_surface_detailed(self, bem, zone, surface):
        """
        :param bem: EnergyPlus model
        :param zone: zone in which the surface is located
        :param surface: surface to be added in the EnergyPlus model
        :return: detailed of the surface
        """
        buidling_surface_detailed = bem.energyplus_objects.BuildingSurface_Detailed.add(
            name = surface.name,
            surface_type = 'Floor',
            construction_name = 'GROUND FLOOR',
            zone_name = zone.name,
            space_name = '',
            outside_boundary_condition = 'Ground',
            outside_boundary_condition_object = '',
            sun_exposure = 'NoSun',
            wind_exposure = 'NoWind',
            view_factor_to_ground = 'autocalculate',
            number_of_vertices = len(surface.points)
        )
        return buidling_surface_detailed

class AddRoofSurfacesEnergyPlusModel(AddSurfacesEnergyPlusModel):
    """
    Class add surfaces in the EnergyPlus model
    """
    def get_surfaces(self, zone):
        """
        :param zone: zone in which the surface is located
        :return: surfaces to be added in the EnergyPlus file
        """
        if len(zone.roof_surfaces) > 0:
            return zone.roof_surfaces
        else:
            return []

    def get_buidling_surface_detailed(self, bem, zone, surface):
        """
        :param bem: EnergyPlus model
        :param zone: zone in which the surface is located
        :param surface: surface to be added in the EnergyPlus model
        :return: detailed of the surface
        """
        buidling_surface_detailed = bem.energyplus_objects.BuildingSurface_Detailed.add(
            name = surface.name,
            surface_type = 'Roof',
            construction_name = 'ROOF',
            zone_name = zone.name,
            space_name = '',
            outside_boundary_condition = 'Outdoors',
            outside_boundary_condition_object = '',
            sun_exposure = 'SunExposed',
            wind_exposure = 'WindExposed',
            view_factor_to_ground = 'autocalculate',
            number_of_vertices = len(surface.points)
        )
        return buidling_surface_detailed

class AddExteriorWallSurfacesEnergyPlusModel(AddSurfacesEnergyPlusModel):
    """
    Class add surfaces in the EnergyPlus model
    """
    def get_surfaces(self, zone):
        """
        :param zone: zone in which the surface is located
        :return: surfaces to be added in the EnergyPlus file
        """
        if len(zone.exterior_wall_surfaces) > 0:
            return zone.exterior_wall_surfaces
        else:
            return []

    def get_buidling_surface_detailed(self, bem, zone, surface):
        """
        :param bem: EnergyPlus model
        :param zone: zone in which the surface is located
        :param surface: surface to be added in the EnergyPlus model
        :return: detailed of the surface
        """
        buidling_surface_detailed = bem.energyplus_objects.BuildingSurface_Detailed.add(
            name = surface.name,
            surface_type = 'Wall',
            construction_name = 'EXTERIOR WALL',
            zone_name = zone.name,
            space_name = '',
            outside_boundary_condition = 'Outdoors',
            outside_boundary_condition_object = '',
            sun_exposure = 'SunExposed',
            wind_exposure = 'WindExposed',
            view_factor_to_ground = 'autocalculate',
            number_of_vertices = len(surface.points)
        )
        return buidling_surface_detailed

class AddOutputVariableEnergyPlusModel(AddBuildingData):
    """
    Class to add an output variable of the EnergyPlus model.
    """
    __metaclass__ = ABCMeta

    def add(self, bem, building):
        """
        Add an output variable into an EnergyPlus model
        :param bem: the EnergyPlus model before adding the output variable
        :param building: the building data containing the output variable
        :return: the building energy model after adding the output variable
        """
        bem.energyplus_objects.Output_Variable.add(
            key_value = '*',
            variable_name = self.get_variable_name(),
            reporting_frequency = 'Timestep',
            schedule_name = ''
        )
        return bem


    @abstractmethod
    def get_variable_name(self):
        """
        :return: name of the variable.
        """
        pass


class AddHeatingLoadEnergyPlusModel(AddOutputVariableEnergyPlusModel):
    """
    Class to add heating load in the EnergyPlus model.
    """

    def get_variable_name(self):
        """
        :return: name of the variable.
        """
        return 'Zone Ideal Loads Zone Total Heating Rate'

class AddCoolingLoadEnergyPlusModel(AddOutputVariableEnergyPlusModel):
    """
    Class to add cooling load in the EnergyPlus model.
    """

    def get_variable_name(self):
        """
        :return: name of the variable.
        """
        return 'Zone Ideal Loads Zone Total Cooling Rate'


def run_energyplus(input_file, weather_data, output_dir='.', expanded_objects=False):
    """
    Run an EnergyPlus model.
    :param input_file: input IDF file
    :param weather_data: weather data
    :param output_dir: output directory
    :param expanded_objects: True if objects of the EnergyPlus model need to be expanded.
    :return: output of EnergyPlus simulations
    """
    in_idf = input_file
    if expanded_objects:
        shutil.copyfile(input_file, 'in.idf')
        shutil.copy(os.getenv('ENERGYPLUS') + '\\ExpandObjects.exe', '.')
        shutil.copy(os.getenv('ENERGYPLUS') + '\\Energy+.idd', '.')
        subprocess.call('ExpandObjects')
        in_idf = "expanded.idf"
    epm = op.Epm.load(in_idf)
    s = op.simulate(epm, weather_data, output_dir)
    eso = s.get_out_eso()
    return eso.get_data()


