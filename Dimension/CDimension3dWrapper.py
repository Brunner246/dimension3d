from typing import List

import cadwork
import dimension_controller as dc


class CPlaneData:
    def __init__(self, aPlaneNormal: cadwork.point_3d, aPlaneOrigin: cadwork.point_3d):
        self.__plane_normal: cadwork.point_3d = aPlaneNormal
        self.__plane: cadwork.point_3d = aPlaneOrigin

    def get_plane_normal(self):
        return self.__plane_normal

    def get_plane(self):
        return self.__plane


class CDimension3dWrapper:
    def __init__(self, aDirection: cadwork.point_3d, aPlaneData: CPlaneData,
                 aDistance: cadwork.point_3d,
                 aDimensionPoints: List[cadwork.point_3d]):
        self.__direction: cadwork.point_3d = aDirection
        self.__plane_normal: cadwork.point_3d = aPlaneData.get_plane_normal()
        self.__plane: cadwork.point_3d = aPlaneData.get_plane()
        self.__distance: cadwork.point_3d = aDistance
        self.__dimension_points: List[cadwork.point_3d] = aDimensionPoints

    def create_dimension(self):
        dc.create_dimension(self.__direction, self.__plane, self.__distance, self.__dimension_points)
