"""
This is the domain object model of the SCIENCE project.

Delft University of Technology
Dr. Miguel Martin
"""
from abc import ABCMeta, abstractmethod
import pytz
from shapely.geometry import Polygon
import numpy as np
from panda3d.core import Triangulator3

from pint import UnitRegistry
ureg = UnitRegistry()
ureg.default_format = '.3f'
Q_ = ureg.Quantity

class Point:
    """
    Class representing a 3D point.

    Attributes:
        x: x-coordinate
        y: y-coordinate
        z: z-coordinate
    """

    def __init__(self, x, y, z):
        """
        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        """
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        """
        :param other: other point
        """
        return (self.x == other.x) & (self.y == other.y) & (self.z == other.z)


class Surface:
    """
    Class representing a surface

    Attributs:
        name: name of the surface
        points: list of points
    """
    def __init__(self, name):
        """
        :param name: name of the surface
        """
        self.name = name
        self.points = []

    def __eq__(self, other):
        """
        :param other: other surface
        """
        return (self.name == other.name) & (self.points == other.points)

    def triangulate(self):
        """
        Triangulate the surface
        :return: List of triangles
        """
        trig = Triangulator3()
        for p in self.points:
            vi = trig.add_vertex(p.x, p.y, p.z)
            trig.addPolygonVertex(vi)
        trig.triangulate()
        triangles = []
        for n in range(trig.getNumTriangles()):
            A = trig.get_vertex(trig.getTriangleV0(n))
            B = trig.get_vertex(trig.getTriangleV1(n))
            C = trig.get_vertex(trig.getTriangleV2(n))
            surface = Surface('Triangle ' + str(n))
            surface.points.append(Point(A[0], A[1], A[2]))
            surface.points.append(Point(B[0], B[1], B[2]))
            surface.points.append(Point(C[0], C[1], C[2]))
            triangles.append(surface)
        return triangles



class InteriorSurface(Surface):
    """
    Class representing an interior surface

    Attributes:
        name: name of the interior surface
        connected_interior_surface: connected interior surface
    """

    def __init__(self, name):
        """
        :param name: name of the interior surface
        """
        Surface.__init__(self, name)
        self.connected_interior_surface = None

class ExteriorWall(Surface):
    """
    Class representing an exterior wall surface

    Attributes:
        name: name of the exterior wall surface
        windows: list of windows
        doors: list of doors
    """

    def __init__(self, name):
        """
        :param name: name of the exterior wall surface
        """
        Surface.__init__(self, name)
        self.windows = []
        self.doors = []


class Zone:
    """
    Class representing a zone within a building.

    Attributes:
        name: name of the zone
        roof_surfaces: list of roof surfaces
        exterior_wall_surfaces: list of exterior wall surfaces
        interior_wall_surfaces: list of interior wall surfaces
        ground_floor_surface: ground surface (if any)
        interior_floor_surface: interior floor surface (if any)
        interior_ceiling_surface: interior ceiling surface (if any)
    """

    __area = None
    __volume = None

    def __init__(self, name):
        """
        :param name: name of the zone
        """
        self.name = name
        self.roof_surfaces  = []
        self.exterior_wall_surfaces = []
        self.interior_wall_surfaces = []
        self.ground_floor_surface = None
        self.interior_floor_surface = None
        self.interior_ceiling_surface = None

    def get_area(self):
        """
        :return: the area of the zone (in meter ** 2)
        """
        if self.__area is None:
            if not self.ground_floor_surface is None:
                floor_surface = self.ground_floor_surface
            else:
                floor_surface = self.interior_floor_surface
            polygon = Polygon([[p.x, p.y] for p in floor_surface.points])
            self.__area = Q_(polygon.area, ureg.meter ** 2)
        return self.__area

    def get_volume(self):
        """
        :return: the volume of the zone (in meter ** 3)
        """
        if self.__volume is None:
            self.__volume = 0.0
            surfaces = self.roof_surfaces + \
                       self.exterior_wall_surfaces + \
                       self.interior_wall_surfaces + \
                       [self.ground_floor_surface] + \
                       [self.interior_floor_surface] + \
                       [self.interior_ceiling_surface]
            for s in surfaces:
                if not s is None:
                    for triangle in s.triangulate():
                        A = np.array([triangle.points[0].x, triangle.points[0].y, triangle.points[0].z])
                        B = np.array([triangle.points[1].x, triangle.points[1].y, triangle.points[1].z])
                        C = np.array([triangle.points[2].x, triangle.points[2].y, triangle.points[2].z])
                        self.__volume = self.__volume + np.dot(A, np.cross(B, C))
            self.__volume = Q_((1.0 / 6.0) * self.__volume, ureg.meter ** 2)
        return self.__volume

class Location():
    """
    Class representing the location of a building

    Attributes:
        name : name of the location
        latitude: latitude of the location (in degree)
        longitude: longitude of the location (in degree)
        timezone: time zone of the location
        altitude: altitude of the location (in meter)
    """

    def __init__(self, name):
        """
        :param name: name of the location
        """
        self.name = name
        self.latitude = Q_(0.0, ureg.deg)
        self.longitude = Q_(0.0, ureg.deg)
        self.timezone = pytz.timezone('Europe/Amsterdam')
        self.altitude = Q_(0.0, ureg.meter)

class Building:
    """
    Class representing a building

    Attributes:
        name: name of the building
        location: location of the building
        zones: list of zones contained in the building
    """

    def __init__(self, name):
        """
        :param name: name of the building
        """
        self.name = name
        self.location = None
        self.zones = []