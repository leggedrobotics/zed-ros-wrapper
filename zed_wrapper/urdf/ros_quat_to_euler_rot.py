import tf
from tf.transformations import *

# =============================================================================
# Quaternions, Euler angles, and axis order conventions
# =============================================================================

# Quaternion convention:
#   [x, y, z, w] where q = x*i + y*j + z*k + w

# Euler axis convention (24 possibilities):
#   4-character string (e.g., 'sxyz', 'ryxy') or encoded 4-tuple:
#     * First char:  's' = static frame,  'r' = rotating frame
#     * Next 3 chars: Axis sequence ('x', 'y', 'z')
#
#   Encoded 4-tuple:
#     (axis, parity, repetition, frame)
#       axis: {'x':0, 'y':1, 'z':2}
#       parity: even=0, odd=1 (see tf docs for rules)
#       repetition: 1 if first and last axes are same, else 0
#       frame: static=0, rotating=1

# Reference:
#   https://github.com/ros/geometry/blob/noetic-devel/tf/src/tf/transformations.py#L1089

def compare_lists(a, b, tol=1e-6):
    return all(abs(x - y) < tol for x, y in zip(a, b))

# =============================================================================
# Example 1: Quaternion to Euler (default axes 'sxyz') and back
# =============================================================================

q1 = [-0.00183512, 0.000211432, -0.00651105, 0.999977]   # [x, y, z, w]
axes1 = 'sxyz'
euler1 = euler_from_matrix(quaternion_matrix(q1), axes1)
q1_rec = quaternion_from_euler(*euler1, axes=axes1)
euler1_rec = euler_from_quaternion(q1_rec, axes=axes1)
print(f"Example 1")
print(f"  Quaternion: {q1}")
print(f"  → Euler ({axes1}): {euler1}")
print(f"  → Quaternion (from euler): {q1_rec}")
print(f"  → Euler (from quaternion): {euler1_rec}")
print(f"  Close to original quaternion? {compare_lists(q1, q1_rec)}")
print(f"  Close to original euler? {compare_lists(euler1, euler1_rec)}\n")

# =============================================================================
# Example 2: Quaternion to Euler with non-standard axes and back
# =============================================================================

q2 = [0.06146124, 0, 0, 0.99810947]
axes2 = 'syxz'
euler2 = euler_from_matrix(quaternion_matrix(q2), axes2)
q2_rec = quaternion_from_euler(*euler2, axes=axes2)
euler2_rec = euler_from_quaternion(q2_rec, axes=axes2)
print(f"Example 2")
print(f"  Quaternion: {q2}")
print(f"  → Euler ({axes2}): {euler2}")
print(f"  → Quaternion (from euler): {q2_rec}")
print(f"  → Euler (from quaternion): {euler2_rec}")
print(f"  Close to original quaternion? {compare_lists(q2, q2_rec)}")
print(f"  Close to original euler? {compare_lists(euler2, euler2_rec)}\n")

# =============================================================================
# Example 3: Euler to Quaternion and back
# =============================================================================

euler3 = (0.1, 0.2, 0.3)
axes3 = 'rzyx'
q3 = quaternion_from_euler(*euler3, axes=axes3)
euler3_rec = euler_from_quaternion(q3, axes=axes3)
q3_rec = quaternion_from_euler(*euler3_rec, axes=axes3)
print(f"Example 3")
print(f"  Euler ({axes3}): {euler3}")
print(f"  → Quaternion: {q3}")
print(f"  → Euler (from quaternion): {euler3_rec}")
print(f"  → Quaternion (from euler): {q3_rec}")
print(f"  Close to original quaternion? {compare_lists(q3, q3_rec)}")
print(f"  Close to original euler? {compare_lists(euler3, euler3_rec)}\n")

# =============================================================================
# Example 4: Explicit axes tuple (equivalent to 'sxyz'), back and forth
# =============================================================================

q4 = [0.0, 0.7071068, 0.0, 0.7071068]
axes4 = (0, 0, 0, 0)  # (axis=x, parity=even, repetition=no, frame=static)
euler4 = euler_from_quaternion(q4, axes=axes4)
q4_rec = quaternion_from_euler(*euler4, axes=axes4)
euler4_rec = euler_from_quaternion(q4_rec, axes=axes4)
print(f"Example 4")
print(f"  Quaternion: {q4}")
print(f"  → Euler (axes={axes4}): {euler4}")
print(f"  → Quaternion (from euler): {q4_rec}")
print(f"  → Euler (from quaternion): {euler4_rec}")
print(f"  Close to original quaternion? {compare_lists(q4, q4_rec)}")
print(f"  Close to original euler? {compare_lists(euler4, euler4_rec)}\n")

# =============================================================================
# Example 5: Compose rotation matrices then convert to Euler and back
# =============================================================================

R1 = rotation_matrix(0.2, (1,0,0))
R2 = rotation_matrix(0.3, (0,1,0))
R3 = rotation_matrix(0.4, (0,0,1))
R = concatenate_matrices(R1, R2, R3)
axes5 = 'sxyz'
euler5 = euler_from_matrix(R, axes=axes5)
R_rec = euler_matrix(*euler5, axes=axes5)
euler5_rec = euler_from_matrix(R_rec, axes=axes5)
print(f"Example 5")
print(f"  Rotation Matrix (X=0.2, Y=0.3, Z=0.4)")
print(f"  → Euler (sxyz): {euler5}")
print(f"  → Rotation matrix (from euler):\n{R_rec}")
print(f"  → Euler (from matrix): {euler5_rec}")
print(f"  Close to original euler? {compare_lists(euler5, euler5_rec)}\n")
