# Written by: Michael Brunner

from typing import List

import cadwork
import element_controller as ec
import dimension_controller as dc

from Plane.CPlane3D import CPlane3D


class CDimension3dWrapper:
    """Wrapper class for cadwork dimension element"""

    def __init__(self, aDirection: cadwork.point_3d, aPlaneData: CPlane3D,
                 aDistance: cadwork.point_3d,
                 aDimensionPoints: List[cadwork.point_3d]):

        self.__direction: cadwork.point_3d = aDirection
        self.__plane_normal: cadwork.point_3d = aPlaneData.get_normal_vector()
        self.__plane: cadwork.point_3d = aPlaneData.get_plane()
        self.__distance: cadwork.point_3d = aDistance
        self.__dimension_points: List[cadwork.point_3d] = aDimensionPoints
        self.__dimension_element_id: int = 0

        if (len(self.__dimension_points) < 2):
            raise ValueError("Dimension needs at least two points")

    def create_dimension(self):
        self.__dimension_element_id = dc.create_dimension(self.__direction,
                                                          self.__plane_normal,
                                                          self.__plane,
                                                          self.__distance,
                                                          self.__dimension_points)

    def get_dimension_element_id(self):
        return self.__dimension_element_id

    def set_dimension_element_id(self, aDimensionElementId: int):
        if (ec.check_element_id(self.__dimension_element_id) == False):
            raise ValueError("Invalid dimension element id")
        self.__dimension_element_id = aDimensionElementId

    def set_orientation(self, aViewDirection: cadwork.point_3d, aViewUpDirection: cadwork.point_3d):
        if (self.__dimension_element_id == 0):
            raise ValueError("Dimension has to be created first")
        print(f"set orientation for dimension {self.__dimension_element_id}")
        dc.set_orientation([self.__dimension_element_id], aViewDirection, aViewUpDirection)

    def add_segment(self, aDimensionSegment: cadwork.point_3d):
        if (self.__dimension_element_id == 0):
            raise ValueError("Dimension has to be created first")
        print(f"add segment to dimension {self.__dimension_element_id}")
        dc.add_segment(self.__dimension_element_id, aDimensionSegment)

    def set_unit_precision(self, aPrecision: int = 1):
        if (self.__dimension_element_id == 0):
            raise ValueError("Dimension has to be created first")
        dc.set_precision([self.__dimension_element_id], aPrecision)
