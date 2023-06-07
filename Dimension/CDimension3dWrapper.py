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
        self.__plane: CPlane3D = aPlaneData
        self.__distance: cadwork.point_3d = aDistance
        self.__dimension_points: List[cadwork.point_3d] = aDimensionPoints
        self.__dimension_element_id: int = 0

        if (len(self.__dimension_points) < 2):
            raise ValueError("Dimension needs at least two points")

    def create_dimension(self):
        self.__dimension_element_id = dc.create_dimension(self.__direction,
                                                          self.__plane.get_normal(),
                                                          self.__plane.get_plane_origin(),
                                                          self.__distance,
                                                          self.__dimension_points)

    def get_dimension_element_id(self):
        return self.__dimension_element_id

    def set_dimension_element_id(self, aDimensionElementId: int):
        self.__validate_element_id()
        self.__dimension_element_id = aDimensionElementId

    def get_dimension_normal(self) -> cadwork.point_3d:
        return self.__plane.get_normal()

    def get_dimension_plane(self) -> cadwork.point_3d:
        return self.__plane.get_plane_origin()

    def set_orientation(self, aViewDirection: cadwork.point_3d, aViewUpDirection: cadwork.point_3d):
        self.__validate_element_id()
        print(f"set orientation for dimension {self.__dimension_element_id}")
        dc.set_orientation([self.__dimension_element_id], aViewDirection, aViewUpDirection)

    def add_segment(self, aDimensionSegment: cadwork.point_3d):
        self.__validate_element_id()
        dc.add_segment(self.__dimension_element_id, aDimensionSegment)

    def __validate_element_id(self):
        """Check if element id is valid
        :raises ValueError: if element id is invalid
        handle in production code with try/except"""
        if not ec.check_element_id(self.__dimension_element_id):
            raise ValueError(f"invalid element id: {self.__dimension_element_id}")

    def set_unit_precision(self, aPrecision: int = 1):
        self.__validate_element_id()
        dc.set_precision([self.__dimension_element_id], aPrecision)

    def set_text_size(self, aTextSize: float):
        self.__validate_element_id()
        dc.set_text_size([self.__dimension_element_id], aTextSize)

    def set_line_thickness(self, aLineThickness: float):
        self.__validate_element_id()
        dc.set_line_thickness([self.__dimension_element_id], aLineThickness)

    def set_total_dimension(self, aTotalDimension: bool = True):
        self.__validate_element_id()
        dc.set_total_dimension([self.__dimension_element_id], aTotalDimension)

    def set_text_color(self, aColorNr: int):
        self.__validate_element_id()
        dc.set_text_color([self.__dimension_element_id], aColorNr)

    def set_line_color(self, aColorNr: int):
        self.__validate_element_id()
        dc.set_line_color([self.__dimension_element_id], aColorNr)

    def set_default_anchor_length(self, aAnchorLength: float):
        self.__validate_element_id()
        dc.set_default_anchor_length([self.__dimension_element_id], aAnchorLength)