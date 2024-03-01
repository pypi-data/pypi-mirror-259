"""
This is the domain object model of the SCIENCE project.

Delft University of Technology
Dr. Miguel Martin
"""
from abc import ABCMeta, abstractmethod
import numpy as np
import pyny3d.geoms as pyny
from panda3d.core import Triangulator3

from pint import UnitRegistry
ureg = UnitRegistry()
ureg.default_format = '.3f'
Q_ = ureg.Quantity

class IDObject():
    """
    Object identified by a name

    Attributs:
        name: name of the object
    """
    __metaclass__ = ABCMeta

    def __init__(self, name):
        """
        :param name: name of the object
        """
        self.name = name

class Surface(IDObject, pyny.Polygon):
    """
    Class representing a surface

    Attributs:
        name: name of the surface
        points: list of points
        temperature: temperature of the surface [in degree Celsius]
    """
    __area = None

    def __init__(self, name, points):
        """
        :param name: name of the surface
        :param points: points delimiting the surface
        """
        IDObject.__init__(self, name)
        pyny.Polygon.__init__(self, points, make_ccw = False)
        self.temperature = None

    def __eq__(self, other):
        """
        :param other: other surface
        """
        return (self.name == other.name) & \
               (np.all(self.points == other.points)) & \
               (self.temperature == other.temperature)

    def triangulate(self):
        """
        Triangulate the surface
        :return: list of triangles
        """
        trig = Triangulator3()
        for p in self.points:
            vi = trig.add_vertex(p[0], p[1], p[2])
            trig.addPolygonVertex(vi)
        trig.triangulate()
        triangles = []
        for n in range(trig.getNumTriangles()):
            points = np.array([trig.get_vertex(trig.getTriangleV0(n)),
                               trig.get_vertex(trig.getTriangleV1(n)),
                               trig.get_vertex(trig.getTriangleV2(n))])
            surface = Surface('Triangle ' + str(n), points)
            triangles.append(surface)
        return triangles
    def get_area(self):
        """
        :return: area of the surface (in meter ** 2)
        """
        if self.__area is None:
            num_points = len(self.points)
            if num_points == 3:
                area = pyny.Polygon.get_area(self)
            else:
                area = 0.0
                for triangle in self.triangulate():
                    area = area + triangle.get_area()
            self.__area = Q_(area, ureg.meter ** 2)
        return self.__area

    def move(self, dx, dy, dz = 0.0):
        """
        Move the surface to a certain position.
        :param dx: distance to move in the x-axis.
        :param dy: distance to move in the y-axis.
        :param dz: distance to move in the z-axis.
        :return: the surface after being moved.
        """
        polygon = pyny.Polygon(self.points, make_ccw = False).move((dx, dy, dz))
        surface = Surface(self.name, polygon.points)
        surface.temperature = self.temperature
        return surface

class ExteriorWall(Surface):
    """
    Class representing an exterior wall surface

    Attributes:
        name: name of the exterior wall surface
        points: points delimiting the exterior surface
        temperature: temperature of the surface [in degree Celsius]
        windows: list of windows
        doors: list of doors
    """
    __wall_area = None

    def __init__(self, name, points):
        """
        :param name: name of the exterior wall surface
        :param points: points delimiting the exterior surface
        """
        Surface.__init__(self, name, points)
        self.windows = []
        self.doors = []

    def __eq__(self, other):
        """
        :param other: other surface
        """
        return Surface.__eq__(self, other) & \
               (self.windows == other.windows) & \
               (self.doors == other.doors)

    def get_wall_area(self):
        """
        :return: the area that is made of wall only (in meter ** 2)
        """
        if self.__wall_area is None:
            wall_area = self.get_area()
            for win in self.windows:
                wall_area = wall_area - win.get_area()
            for door in self.doors:
                wall_area = wall_area - door.get_area()
            self.__wall_area = Q_(wall_area, ureg.meter ** 2)
        return self.__wall_area

    def move(self, dx, dy, dz = 0.0):
        """
        Move the external wall to a certain position.
        :param dx: distance to move in the x-axis.
        :param dy: distance to move in the y-axis.
        :param dz: distance to move in the z-axis.
        :return: the surface after being moved.
        """
        surface = Surface(self.name, self.points).move(dx, dy, dz)
        exterior_wall = ExteriorWall(surface.name, surface.points)
        exterior_wall.temperature = surface.temperature
        exterior_wall.windows = []
        for win in self.windows:
            exterior_wall.windows.append(win.move(dx, dy, dz))
        for door in self.doors:
            exterior_wall.doors.append(door.move(dx, dy, dz))
        return exterior_wall

class Air():
    """
    Volume of air

    Attribute:
        temperature: temperature of the air volume (in degree Celsius)
        humidity: humidity of the air volume (in kilogram of water per kilogram of air)
    """
    __metaclass__ = ABCMeta
    __volume = None

    def __init__(self):
        self.temperature = None
        self.humidity = None

    def get_volume(self):
        """
        :return: the volume of air (in meter ** 3)
        """
        if self.__volume is None:
            self.__volume = Q_(self.compute_volume(), ureg.meter ** 3)
        return self.__volume

    @abstractmethod
    def compute_volume(self):
        """
        :return: the calcuated volume of air
        """
        pass

class Zone(IDObject, Air):
    """
    Class representing a zone within a building.

    Attributes:
        name: name of the zone
        temperature: temperature in the zone (in degree Celsius)
        humidity: humidity in the zone (in kilogram of water per kilogram of air)
        roofs: list of roof surfaces
        exterior_walls: list of exterior wall surfaces
        ground_floor: ground surface
        sensible_cooling_load: sensible cooling load in the zone (in watts)
        latent_cooling_load: latent cooling load in the zone (in watts)
    """

    def __init__(self, name):
        """
        :param name: name of the zone
        """
        IDObject.__init__(self, name)
        Air.__init__(self)
        self.roofs = []
        self.exterior_walls = []
        self.ground_floor = None
        self.sensible_cooling_load = None
        self.latent_cooling_load = None

    def compute_volume(self):
        """
        :return: compute the volume of air in the zone
        """
        volume = 0.0
        surfaces = self.roofs + \
                   self.exterior_walls + \
                   [self.ground_floor]
        for s in surfaces:
            for triangle in s.triangulate():
                A = np.array([triangle.points[0][0], triangle.points[0][1], triangle.points[0][2]])
                B = np.array([triangle.points[1][0], triangle.points[1][1], triangle.points[1][2]])
                C = np.array([triangle.points[2][0], triangle.points[2][1], triangle.points[2][2]])
                volume = volume + np.abs(np.dot(A, np.cross(B, C)))
        volume = (1.0 / 6.0) * volume
        return volume
    def aspolyhedron(self):
        """
        Express the zone as a polyhedron (pyny3d.geoms.Polyhedron)
        """
        polygons = []
        for roof in self.roofs:
            polygons.append(pyny.Polygon(roof.points, make_ccw = False))
        for exterior_wall in self.exterior_walls:
            polygons.append(pyny.Polygon(exterior_wall.points, make_ccw = False))
        polygons.append(pyny.Polygon(self.ground_floor.points, make_ccw = False))
        return pyny.Polyhedron(polygons)

    def move(self, dx, dy, dz = 0.0):
        """
        Move the zone to a certain position.
        :param dx: distance to move in the x-axis.
        :param dy: distance to move in the y-axis.
        :param dz: distance to move in the z-axis.
        """
        for n in range(len(self.roofs)):
            self.roofs[n] = self.roofs[n].move(dx, dy, dz)
        for n in range(len(self.exterior_walls)):
            self.exterior_walls[n] = self.exterior_walls[n].move(dx, dy, dz)
        self.ground_floor = self.ground_floor.move(dx, dy, dz)


class Building(IDObject):
    """
    Class representing a building

    Attributes:
        name: name of the building
        zones: zones of the building
    """

    def __init__(self, name):
        """
        :param name: name of the building
        """
        IDObject.__init__(self, name)
        self.zones = []

    def move(self, dx, dy, dz = 0.0):
        """
        Move the building to a certain position.
        :param dx: distance to move in the x-axis.
        :param dy: distance to move in the y-axis.
        :param dz: position to move in the z-axis.
        """
        for zone in self.zones:
            zone.move(dx, dy, dz)

    def get_exterior_wall(self, exterior_wall_name):
        """
        :param exterior_wall_name: name of the exterior wall
        :return: extrior wall of the building
        """
        extrior_wall_building = None
        is_extrior_wall_found = False
        for zone in self.zones:
            for extrior_wall in zone.exterior_walls:
                if extrior_wall.name == exterior_wall_name:
                    extrior_wall_building = extrior_wall
                    is_extrior_wall_found = True
                    break
            if is_extrior_wall_found: break
        return extrior_wall_building

    def get_footprint(self):
        polygons = []
        for zone in self.zones:
            if zone.ground_floor is not None:
                polygons.append(pyny.Polygon(zone.ground_floor.points, make_ccw = False))
        return pyny.Surface(polygons, melt = True)


class Atmosphere(Air):
    """
    Class representing the atmosphere above an urban area

    Attributes:
        temperature: air temperature in the atmosphere (in degree Celsius)
        humidity: air specific humidity in the atmosphere (in kilogram of water per kilogram of air)
    """

    def __init__(self):
        Air.__init__(self)

    def compute_volume(self):
        """
        :return: the calcuated volume of air in the atmosphere
        """
        return 0.0


class HeatSource(IDObject):
    """
    Class representing a source of  heat

    Attribute:
        name: name of the heat source
        sensible_heat: sensible heat released from the source [in watts]
        latent_heat: latent heat released from the source [in watts]
    """

    __metaclass__ = ABCMeta

    def __init__(self, name):
        """
        :param name: name of the anthropogenic heat source
        """
        IDObject.__init__(self, name)
        self.sensible_heat = None
        self.latent_heat = None

class WasteHeat(HeatSource):
    """
    Class representing waste heat caused by one or several buildings

    Attribute:
        name: name of the source of waste heat
        buildings: list of buildings responsible of the waste heat
    """

    def __init__(self, name):
        """
        :param name: name of the waste heat source
        """
        HeatSource.__init__(self, name)
        self.buildings = []

class Traffic(HeatSource):
    """
    Class representing traffic

    Attribute:
        name: name of the traffic
    """

    def __init__(self, name):
        """
        :param name: name of the traffic
        """
        HeatSource.__init__(self, name)

class Vegetation(Surface):
    """
        Class representing vegetation

        Attribute:
            name: name of the vegetation
            points: points delimiting the vegetation
            lai: leaf area index of the vegetation (in meter per meter)
        """

    def __init__(self, name, points, lai):
        """
        :param name: name of the vegetation
        :param points: points delimiting the vegetation
        """
        Surface.__init__(self, name, points)
        self.lai = lai

class SurroundingWall(ExteriorWall):
    """
        Class representing an exterior wall surrounding a street canyon

        Attributes:
            name: name of the surrounding wall
            points: points delimiting the surrounding wall
            temperature: temperature of the surface [in degree Celsius]
            windows: list of windows
            doors: list of doors
            building: building of the surrounding wall
    """
    def __init__(self, exterior_wall_name, building):
        """
        :param name: name of the street canyon
        :param points: points delimiting the surrounding wall
        :param building: building of the surrounding wall
        """
        exterior_wall = building.get_exterior_wall(exterior_wall_name)
        ExteriorWall.__init__(self, exterior_wall.name, exterior_wall.points)
        self.temperature = exterior_wall.temperature
        self.windows = exterior_wall.windows
        self.doors = exterior_wall.doors
        self.building = building

class WeatherStation(IDObject):
    """
    Class representing a street canyon

    Attributes:
        name: name of the weather station
        temperature: air temperature recorded by the weather station (in degree Celsius)
        humidity: air relative humidity recorded by the weather station (in %)
        pressure: air pressure recorded by the weather station (in hPa)
    """

    def __init__(self, name):
        """
        :param name: name of the street canyon
        """
        IDObject.__init__(self, name)
        self.temperature = None
        self.humidity = None
        self.pressure = None


class StreetCanyon(IDObject, Air):
    """
    Class representing a street canyon

    Attributes:
        name: name of the street canyon
        pavements: pavements of the street canyon
        surrounding_walls: surrounding walls of the street canyon
        atmosphere: atmospheric conditions above the street canyon
        waste_heat_sources: sources of waste heat around the street canyon
        traffic: traffic in the street canyon
        vegetation: vegetation in the street canyon
        weather_stations: weather stations located in the street canyon
    """
    __surface = None
    __height = Q_(-1.0, ureg.meter)

    def __init__(self, name):
        """
        :param name: name of the street canyon
        """
        IDObject.__init__(self, name)
        Air.__init__(self)
        self.atmosphere = None
        self.pavements = []
        self.surrounding_walls = []
        self.waste_heat_sources = []
        self.traffic = []
        self.vegetation = []
        self.weather_stations = []

    def get_surface(self):
        """
        :return: bottom surface of the street canyon.
        """
        if self.__surface is None:
            points = []
            for sw in self.surrounding_walls:
                npoints = sw.points.shape[0]
                for n in range(npoints):
                    if sw.points[n, 2] == 0.0:
                        points.append(sw.points[n].tolist())
            points = np.unique(np.array(points), axis=0)
            cx, cy, cz = points.mean(0)
            x, y, z = points.T
            angles = np.arctan2(x - cx, y - cy)
            indices = np.argsort(angles)
            self.__surface = Surface(self.name + ':surface', points[indices])
        return self.__surface

    def get_height(self):
        """
        :return: height of the street canyon [in meter].
        """
        if self.__height.m < 0.0:
            self.__height = Q_(0.0, ureg.meter)
            for sw in self.surrounding_walls:
                npoints = sw.points.shape[0]
                for n in range(npoints):
                    if sw.points[n, 2] > self.__height.m:
                        self.__height = Q_(sw.points[n, 2], ureg.meter)
        return self.__height

    def compute_volume(self):
        """
        :return: the calcuated volume of air
        """
        return self.get_surface().get_area().m * self.get_height().m

    def get_buildings(self):
        """
        :return: buildings connected to the street canyon
        """
        buildings = []
        building_names = []
        for sw in self.surrounding_walls:
            if not sw.building.name in building_names:
                buildings.append(sw.building)
                building_names.append(sw.building.name)
        return buildings


class Neighborhood(IDObject):
    """
    Class representing a neighborhood

    Attributes:
        name: name of the neighborhood
        buildings: buildings in the neighborhood
        street_canyons: street canyons in the neighborhood
    """

    def __init__(self, name):
        """
        :param name: name of the neighborhood
        """
        IDObject.__init__(self, name)
        self.street_canyons = []

    def get_buildings(self):
        """
        :return: buildings connected to the street canyon
        """
        buildings = []
        building_names = []
        for sc in self.street_canyons:
            for b in sc.get_buildings():
                if not b.name in building_names:
                    buildings.append(b)
                    building_names.append(b.name)
        return buildings

