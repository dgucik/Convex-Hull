import pygame.display

from points_array import PointsArray
from relative_point import RelativePoint
from text_object import TextObject


class MainWindow:
    def __init__(self, window_size):
        self.window_size = window_size
        self.background_color = (255, 255, 255)

        self.origin_x = self.window_size[0] // 2
        self.origin_y = self.window_size[1] // 2

        self.axis_color = (150, 150, 150)
        self.axis_color2 = (230, 230, 230)
        self.text_color = (150, 150, 150)
        self.text_color2 = (50, 50, 50)

        self.font = pygame.font.SysFont("arial", 10, True, False)
        self.font2 = pygame.font.SysFont("arial", 15, True, False)

        self.pixels_per_inc = 20  # should not be changed
        self.one_inc_value = 1

        self.screen = pygame.display.set_mode(self.window_size)

        self.tab_pressed = False

    def get_surface(self):
        return self.screen

    def handle_events(self, event):
        if pygame.key.get_pressed()[pygame.K_TAB]:
            self.tab_pressed = True
        else:
            self.tab_pressed = False

    def update(self):
        max_point_y = self.one_inc_value * 19
        max_point_x = self.one_inc_value * 28
        for point in PointsArray.array:
            if abs(point[0]) > max_point_x:
                max_point_x = abs(point[0])
            if abs(point[1]) > max_point_y:
                max_point_y = abs(point[1])

        if max_point_y > self.one_inc_value * 19 and max_point_x > self.one_inc_value * 28:
            if (max_point_y - self.one_inc_value * 19) > (max_point_x - self.one_inc_value * 28):
                self.one_inc_value = max_point_y // 19
            elif (max_point_x - self.one_inc_value * 28) > (max_point_y - self.one_inc_value * 19):
                self.one_inc_value = max_point_y // 28
            else:
                self.one_inc_value = max_point_y // 19
        elif max_point_y > self.one_inc_value * 19:
            self.one_inc_value = max_point_y // 19
        elif max_point_x > self.one_inc_value * 28:
            self.one_inc_value = max_point_x // 19

    def draw(self):
        self.screen.fill(self.background_color)

        pygame.draw.line(self.screen, self.axis_color, (0, self.origin_y), (self.window_size[0], self.origin_y), 2)
        pygame.draw.line(self.screen, self.axis_color, (self.origin_x, 0), (self.origin_x, self.window_size[1]), 2)

        for x in range(0, self.window_size[0], self.pixels_per_inc):
            pygame.draw.line(self.screen, self.axis_color2, (x, 0), (x, self.window_size[1]), 1)
            pygame.draw.line(self.screen, self.axis_color, (x, self.origin_y - 5), (x, self.origin_y + 5), 2)
        for y in range(0, self.window_size[1], self.pixels_per_inc):
            pygame.draw.line(self.screen, self.axis_color2, (0, y), (self.window_size[0], y), 1)
            pygame.draw.line(self.screen, self.axis_color, (self.origin_x - 5, y), (self.origin_x + 5, y), 2)

        TextObject.draw_text_object(self.screen, f"{self.one_inc_value}",
                                    RelativePoint.point(self.window_size, self.pixels_per_inc, -self.pixels_per_inc),
                                    self.font, self.text_color)

        TextObject.draw_text_object(self.screen, f"{self.one_inc_value}",
                                    RelativePoint.point(self.window_size, -self.pixels_per_inc, self.pixels_per_inc),
                                    self.font, self.text_color)

        TextObject.draw_text_object(self.screen, "x",
                                    RelativePoint.point(self.window_size,
                                                        (self.window_size[0] // 2) - self.pixels_per_inc,
                                                        -1.5 * self.pixels_per_inc),
                                    self.font2, self.text_color2)

        TextObject.draw_text_object(self.screen, "y",
                                    RelativePoint.point(self.window_size, -2 * self.pixels_per_inc,
                                                        (self.window_size[1] // 2) - (self.pixels_per_inc // 2)),
                                    self.font2, self.text_color2)

        PointsArray.draw_points(self.screen, self.pixels_per_inc, self.one_inc_value, self.tab_pressed)
