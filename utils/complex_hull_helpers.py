from containters.point_collection import PointCollection
from utils.complex_hull import Point
import numpy as np
import pygame

from utils.relative_point import RelativePoint

LINE_COLOR = (0, 0, 255)
LINE_WIDTH = 2

def convert_to_point(l):
    result = []
    for x in l:
        result.append(Point(x[0], x[1]))
    return np.array(result)


def convert_to_point_reverse(hh):
    result = []
    for p in hh:
        result.append((p.x, p.y))
    return result


def convex_hull_draw(screen, points):
    for i in range(len(points) - 1):

        # Obliczenie pozycji punktów w układzie
        p1_x_pos = (points[i][0] * PointCollection.grid_unit_size) // PointCollection.grid_unit
        p1_y_pos = (points[i][1] * PointCollection.grid_unit_size) // PointCollection.grid_unit
        p1 = RelativePoint.calculate_point(screen.get_size(), p1_x_pos, p1_y_pos)

        p2_x_pos = (points[i+1][0] * PointCollection.grid_unit_size) // PointCollection.grid_unit
        p2_y_pos = (points[i+1][1] * PointCollection.grid_unit_size) // PointCollection.grid_unit
        p2 = RelativePoint.calculate_point(screen.get_size(), p2_x_pos, p2_y_pos)

        # Rysowanie linii łączącej punkty
        pygame.draw.line(screen, LINE_COLOR, p1, p2, LINE_WIDTH)

    if len(points) >= 3:
        # Obliczenie pozycji pierwszego i ostatniego punktu w układzie
        p1_x_pos = (points[0][0] * PointCollection.grid_unit_size) // PointCollection.grid_unit
        p1_y_pos = (points[0][1] * PointCollection.grid_unit_size) // PointCollection.grid_unit
        p1 = RelativePoint.calculate_point(screen.get_size(), p1_x_pos, p1_y_pos)

        p2_x_pos = (points[-1][0] * PointCollection.grid_unit_size) // PointCollection.grid_unit
        p2_y_pos = (points[-1][1] * PointCollection.grid_unit_size) // PointCollection.grid_unit
        p2 = RelativePoint.calculate_point(screen.get_size(), p2_x_pos, p2_y_pos)

        # Rysowanie linii łączącej pierwszy i ostatni punkt
        pygame.draw.line(screen, LINE_COLOR, p1, p2, LINE_WIDTH)