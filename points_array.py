import pygame

from relative_point import RelativePoint
from text_object import TextObject


class PointsArray:
    array = []
    inc_value = 1

    @staticmethod
    def add_point(point):
        PointsArray.array.append(point)

    @staticmethod
    def clear_array():
        PointsArray.array.clear()

    @staticmethod
    def draw_points(screen, pixels, show_cords = False):
        for point in PointsArray.array:
            x_pos = (point[0] * pixels) // PointsArray.inc_value
            y_pos = (point[1] * pixels) // PointsArray.inc_value
            pygame.draw.circle(screen, (255, 0, 0), RelativePoint.point(screen.get_size(), x_pos, y_pos), 5)
            if show_cords:
                TextObject.draw_text_object(screen, f"({point[0]}, {point[1]})", RelativePoint.point(screen.get_size(), x_pos, y_pos + 5),
                                            pygame.font.SysFont("arial", 14, False, False), (0, 0, 0))