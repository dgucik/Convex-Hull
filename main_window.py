import pygame.display

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

    def get_surface(self):
        return self.screen

    def handle_events(self, event_type):
        pass

    def update(self):
        pass

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