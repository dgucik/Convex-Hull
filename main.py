import pygame
from windows.main_window import MainWindow
from windows.sub_window import SubWindow


class Application:
    def __init__(self, width, height, name):
        """
        Klasa reprezentująca aplikację.

        :param width: Szerokość głównego okna aplikacji.
        :param height: Wysokość głównego okna aplikacji.
        :param name: Nazwa aplikacji.
        """
        # Inicjalizacja rozmiaru i nazwy okna
        self.window_size = (width, height)
        self.name = name

        # Inicjalizacja modułu pygame oraz ustawienie nazwy okna
        pygame.init()
        pygame.display.set_caption(self.name)

        # Ustawienie flagi sygnalizującej że program jest w trakcie działania
        self.running = True

        # Utworzenie głównego okna oraz podokna aplikacji
        self.main_window = MainWindow(self.window_size)
        self.sub_window = SubWindow(self.window_size)

    def __handle_events(self):
        """
        Obsługuje zdarzenia Pygame, takie jak naciśnięcie przycisku myszy czy zamknięcie okna.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.main_window.handle_events(event)
            self.sub_window.handle_events(event)

    def __update(self):
        """
        Aktualizuje logikę głównego i podokna aplikacji.
        """
        self.main_window.update()
        self.sub_window.update()

    def __draw(self):
        """
        Renderuje elementy na ekranie.
        """
        self.main_window.draw()
        self.sub_window.draw(self.main_window.get_surface())

        pygame.display.flip()

    def run(self):
        while self.running:
            self.__handle_events()
            self.__update()
            self.__draw()
        pygame.quit()


if __name__ == '__main__':
    app = Application(1200, 800, "Convex hull")
    app.run()