import pygame
from coordinate_system import CoordinateSystem


class MainWindow:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name

        self.background_color = (255, 255, 255)

        self.running = True

        pygame.init()
        pygame.display.set_caption(self.name)

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.coordinate_system = CoordinateSystem(self.width, self.height, self.screen)

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def __update(self):
        self.coordinate_system.update()

    def __draw_surface(self):
        self.screen.fill(self.background_color)

        self.coordinate_system.draw_surface()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.__handle_events()
            self.__update()
            self.__draw_surface()
        pygame.quit()
