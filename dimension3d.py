# Written by: Michael Brunner

import os
import sys
from time import sleep

import utility_controller as uc
import cadwork

PLUGIN_PATH = uc.get_plugin_path()

user_path = os.path.expanduser('~')
SITE_PACKAGES = [os.path.join(user_path, "PycharmProjects", "dimension3d", "Lib", "site-packages")]
PLUGIN_SOURCES = [PLUGIN_PATH]

[(sys.path.append(source), print(f"appending to path: {source}")) for source in \
 PLUGIN_SOURCES + SITE_PACKAGES if source]

from Plane.CPlane3D import CPlane3D
from Dimension.CDimension3dWrapper import CDimension3dWrapper

if __name__ == '__main__':
    print(f'run script {__name__}')

    plane = CPlane3D(cadwork.point_3d(0, 1, 0), cadwork.point_3d(0, 0, 0))
    dimension_points = [cadwork.point_3d(0, 0, 0), cadwork.point_3d(0, 0, 1000)]
    dimension = CDimension3dWrapper(cadwork.point_3d(0, 0, 1), plane, cadwork.point_3d(200, 0, 0),
                                    dimension_points)
    dimension.create_dimension()

    # change orientation of dimension text
    # new_plane = CPlane3D(plane.get_normal_vector().invert(), cadwork.point_3d(0, 0, 1))
    # print(f"new plane: {new_plane.get_plane()}")
    # dimension.set_orientation(new_plane.get_normal_vector(), new_plane.get_plane())

    dimension.set_unit_precision()
