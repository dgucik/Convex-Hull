import pygame


class CoordinateSystem:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen

        self.origin_x = width // 2
        self.origin_y = height // 2

        self.axis_color = (150, 150, 150)

    def update(self):
        pass

    def draw_surface(self):
        pygame.draw.line(self.screen, self.axis_color, (0, self.origin_y), (self.width, self.origin_y), 1)
        pygame.draw.line(self.screen, self.axis_color, (self.origin_x, 0), (self.origin_x, self.height), 1)

        for x in range(0, self.width, 25):
            pygame.draw.line(self.screen, self.axis_color, (x, self.origin_y - 5), (x, self.origin_y + 5), 1)
        for y in range(0, self.height, 25):
            pygame.draw.line(self.screen, self.axis_color, (self.origin_x - 5, y), (self.origin_x + 5, y), 1)
