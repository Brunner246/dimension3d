# dimension3d

# installation
## to run the script you need to install the cwapi3d package and the cadwork 3d version >= 30.0
see link for cwapi3d usage: [cwapi3d-documentation](https://docs.cadwork.com/projects/cwapi3dpython/en/latest/get_started/) 

```bash 
pip install cwapi3d
```

# usage
```python
import os
import sys

import utility_controller as uc
import cadwork

PLUGIN_PATH = uc.get_plugin_path()

user_path = os.path.expanduser('~')
SITE_PACKAGES = [os.path.join(user_path, "SomeFolder", "dimension3d", "Lib", "site-packages")]
PLUGIN_SOURCES = [PLUGIN_PATH]

[(sys.path.append(source), print(f"appending to path: {source}")) for source in \
 PLUGIN_SOURCES + SITE_PACKAGES if source]

from Plane.CPlane3D import CPlane3D
from Dimension.CDimension3dWrapper import CDimension3dWrapper

plane = CPlane3D(cadwork.point_3d(0, 1, 0), cadwork.point_3d(0, 0, 0))
dimension_points = [cadwork.point_3d(0, 0, 0), cadwork.point_3d(0, 0, 1000)]
dimension = CDimension3dWrapper(cadwork.point_3d(0, 0, 1), plane, cadwork.point_3d(200, 0, 0),
                                dimension_points)
dimension.create_dimension()
```

![dimension.png](..%2F..%2F..%2FOneDrive%20-%20Cadwork%2FBilder%2FScreenshots%2Fdimension.png)
