import cadwork
import math


class CPlane3D:
    def __init__(self, normal: cadwork.point_3d, point: cadwork.point_3d):
        self.__normal: cadwork.point_3d = normal
        self.__point: cadwork.point_3d = point

    def get_normal_vector(self):
        return self.__normal

    def get_point_on_plane(self):
        return self.__point

    def get_plane(self):
        return self.__normal, self.__point

    def get_plane_point3d(self):
        return cadwork.point_3d(*self.__point)

    def calculate_distance_from_plane(self, point):
        distance = abs(sum(self.__normal[i] * (point[i] - self.__point[i]) for i in range(3))) \
                   / math.sqrt(sum(self.__normal[i] ** 2 for i in range(3)))

        return distance

    def project_point(self, point):
        plane_distance = sum(self.__normal[i] * self.__point[i] for i in range(3))
        point_distance = sum(self.__normal[i] * point[i] for i in range(3))
        scaling_factor = (plane_distance - point_distance) / sum(self.__normal[i] ** 2 for i in range(3))
        projected_point = [point[i] + scaling_factor * self.__normal[i] for i in range(3)]

        return projected_point
