import tf
from tf.transformations import *

# Quaternions ix+jy+kz+w are represented as [x, y, z, w].


# A triple of Euler angles can be applied/interpreted in 24 ways, which can
# be specified using a 4 character string or encoded 4-tuple:

#   *Axes 4-string*: e.g. 'sxyz' or 'ryxy'

#   - first character : rotations are applied to 's'tatic or 'r'otating frame
#   - remaining characters : successive rotation axis 'x', 'y', or 'z'

#   *Axes 4-tuple*: e.g. (0, 0, 0, 0) or (1, 1, 1, 1)

#   - inner axis: code of axis ('x':0, 'y':1, 'z':2) of rightmost matrix.
#   - parity : even (0) if inner axis 'x' is followed by 'y', 'y' is followed
#     by 'z', or 'z' is followed by 'x'. Otherwise odd (1).
#   - repetition : first and last axis are same (1) or different (0).
#   - frame : rotations are applied to static (0) or rotating (1) frame.


#https://github.com/ros/geometry/blob/hydro-devel/tf/src/tf/transformations.py#L1174

quaternion = [-0.00183512, 0.000211432, -0.00651105, 0.999977]
axes='sxyz'
# angles = euler_from_quaternion([0.06146124, 0, 0, 0.99810947])
myeuler = euler_from_matrix(quaternion_matrix(quaternion), axes)
print(myeuler)
a=5