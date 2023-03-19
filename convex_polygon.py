import numpy as np
import matplotlib.pyplot as plt

'''
This program takes a sequence of points and determines whether it forms a valid convex polygon. If so, determines
whether the points give the polygon in clockwise or counterclockwise order.

UMD Directed Reading Program S2023 - Computational Geometry
Student: Andy Pavlosky
Mentor: Max Springer
'''

CCW = 1
CW = -1
INVALID = 0

# Checks which direction a segment from p to q then q to r would turn. If it turns counterclockwise, return 1. If it
# turns clockwise return -1. If the points are collinear, return 0.
def orient(p: list, q: list, r: list):
    matrix = np.array([[1, p[0], p[1]], [1, q[0], q[1]], [1, r[0], r[1]]])
    determinant = np.linalg.det(matrix)

    if determinant > 0:
        return CCW
    elif determinant < 0:
        return CW
    else:
        return INVALID

# Checks whether the sequence of points define a convex polygon in clockwise or counterclockwise order.
def polygon_orient(points: list):
    if (len(points) < 3):
        return "invalid"

    initial_orient = orient(points[0], points[1], points[2])

    if orient(points[-2], points[-1], points[0]) != initial_orient:
        return "invalid"

    for i in range(1, len(points) - 2):
        direction = orient(points[i], points[i + 1], points[i + 2])
        if direction != initial_orient:
            return "invalid"

        direction2 = orient(points[i - 1], points[i + 1], points[i + 2])
        if direction2 != initial_orient:
            return "invalid"

    if initial_orient == CW:
        return "CW"
    else:
        return "CCW"

# Graph the polygon resulting from a sequence of vertices.
def graph(polygon: list, orient: str):
    polygon.append(polygon[0])

    xs, ys = zip(*polygon)

    plt.figure()
    plt.plot(xs, ys)
    for point in polygon:
        plt.plot(point[0], point[1], 'bo')
    plt.text(1, 1, orient)
    plt.show()

# Given a sequence of points, check whether it creates a valid polygon and if so, check the orientation that the
# points are given in.
if __name__ == '__main__':
    polygon = [[0.5, 3], [2.5, 4.5], [5, 3], [4, 1.5], [2, 1], [0.5, 1.5]]
    orientation = polygon_orient(polygon)
    print(orientation)
    graph(polygon, orientation)
