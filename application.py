import pygame
from main_window import MainWindow
from sub_window import SubWindow


class Application:
    def __init__(self, width, height, name):
        self.window_size = (width, height)
        self.name = name

        self.running = True

        pygame.init()
        pygame.display.set_caption(self.name)

        self.main_window = MainWindow(self.window_size)
        self.sub_window = SubWindow(self.window_size)

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.main_window.handle_events(event)
            self.sub_window.handle_events(event)

    def __update(self):
        self.main_window.update()
        self.sub_window.update()

    def __draw(self):
        self.main_window.draw()
        self.sub_window.draw(self.main_window.get_surface())

        pygame.display.flip()

    def run(self):
        while self.running:
            self.__handle_events()
            self.__update()
            self.__draw()
        pygame.quit()
