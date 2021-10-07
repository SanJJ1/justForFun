import numpy as np
from numpy import sin, cos, arctan, pi
from numpy.linalg import norm


def sum_forces():
    forces = [360, 240, 380]
    angles = [-30, 45, 135]

    # convert to Radians
    angles = [pi / 180 * angle for angle in angles]

    print(angles)
    x = 0
    y = 0
    for f, a in zip(forces, angles):
        x += f * cos(a)
        y += f * sin(a)
    print(x, y)

    print("Magnitude:  ", np.linalg.norm([x, y]))

    print("Angle:   ", np.degrees(arctan(y / x)))


def multidimensional_distance():
    a = np.array([4, -1, -1])
    b = np.array([2, 0, -4])
    c = np.array([3, 5, -1])
    print(np.linalg.norm(b - c))
    print(b - c)


def cross(u, v):
    u = np.array(u)
    v = np.array(v)
    product = np.cross(u, v)
    return product


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            # >>> angle_between((1, 0, 0), (0, 1, 0))
            # 1.5707963267948966
            # >>> angle_between((1, 0, 0), (1, 0, 0))
            # 0.0
            # >>> angle_between((1, 0, 0), (-1, 0, 0))
            # 3.141592653589793
    """
    v1 = np.array(v1)
    v2 = np.array(v2)
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def projection(u, v):
    """
    :param u:
    :param v:
    :return: returns the projection of U onto V
    """
    u = np.array(u)
    v = np.array(v)
    return (np.dot(u, v)/np.sqrt(sum(v**2))**2)*v

def scal(u, v):
    """
    :param u:
    :param v:
    :return: scalar projection of U onto V
    """

    u = np.array(u)
    v = np.array(v)
    return np.linalg.norm(u) * np.cos(angle_between(u, v))


u = [-4, 0, 3]
v = [2, 1, 2]
print(projection(u, v))

print(cross(u, v), norm(cross(u, v)))


