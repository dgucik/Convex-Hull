import pygame.display

from containters.point_collection import PointCollection
from utils.complex_hull_helpers import convex_hull_draw
from utils.relative_point import RelativePoint
from components.text_object import TextObject


class MainWindow:
    def __init__(self, window_size):
        """
        Reprezentuje główne okno aplikacji.

        :param window_size: Rozmiar okna w pikselach (szerokość, wysokość).
        """
        # Ustawienie szerokości okna oraz koloru tła
        self.window_size = window_size
        self.background_color = (255, 255, 255)

        # Współrzędne środek okna
        self.origin_x = self.window_size[0] // 2
        self.origin_y = self.window_size[1] // 2

        # Kolory osi
        self.axis_color = (150, 150, 150)
        self.axis_color2 = (230, 230, 230)

        # Kolory napisów
        self.text_color = (150, 150, 150)
        self.text_color2 = (50, 50, 50)

        # Czcionki napisów
        self.font = pygame.font.SysFont("arial", 10, True, False)
        self.font2 = pygame.font.SysFont("arial", 15, True, False)

        # Ustawienie wartości dla jednego kroku na siatce oraz ilości pikseli przypadających na jeden krok
        PointCollection.grid_unit_size = 20
        PointCollection.grid_unit = 1

        # Inicjalizacja głównego okna
        self.screen = pygame.display.set_mode(self.window_size)

        # Stan przycisku 'Tab'
        self.tab_pressed = False

    def get_surface(self):
        """
        Zwraca powierzchnię ekranu głównego okna.

        :return: Powierzchnia ekranu.
        """
        return self.screen

    def handle_events(self, event):
        """
        Obsługuje zdarzenia Pygame.

        :param event: Zdarzenie Pygame.
        """
        if pygame.key.get_pressed()[pygame.K_TAB]:
            self.tab_pressed = True
        else:
            self.tab_pressed = False

    def update(self):
        """
        Aktualizuje logikę głównego okna.
        """
        # Wyszukanie maksymalnych współrzędnych punktów
        max_point_y = PointCollection.grid_unit * 19
        max_point_x = PointCollection.grid_unit * 28
        for point in PointCollection.points:
            if abs(point[0]) > max_point_x:
                max_point_x = abs(point[0])
            if abs(point[1]) > max_point_y:
                max_point_y = abs(point[1])

        # Dopasowanie jednostki siatki na podstawie maksymalnych wartości punktów
        if max_point_y > PointCollection.grid_unit * 19 and max_point_x > PointCollection.grid_unit* 28:
            if (max_point_y - PointCollection.grid_unit * 19) > (max_point_x - PointCollection.grid_unit * 28):
                PointCollection.grid_unit = max_point_y // 20 + 1
            elif (max_point_x - PointCollection.grid_unit * 28) > (max_point_y - PointCollection.grid_unit * 19):
                PointCollection.grid_unit = max_point_x // 28 + 1
            else:
                PointCollection.grid_unit = max_point_y // 19 + 1
        elif max_point_y > PointCollection.grid_unit * 19:
            PointCollection.grid_unit = max_point_y // 19 + 1
        elif max_point_x > PointCollection.grid_unit * 28:
            PointCollection.grid_unit = max_point_x // 28 + 1


    def draw(self):
        """
        Rysuje elementy na ekranie głównego okna.
        """
        # Wypełnienie tła okna
        self.screen.fill(self.background_color)

        # Narysowanie głównych osi x i y
        pygame.draw.line(self.screen, self.axis_color, (0, self.origin_y), (self.window_size[0], self.origin_y), 2)
        pygame.draw.line(self.screen, self.axis_color, (self.origin_x, 0), (self.origin_x, self.window_size[1]), 2)

        # Dodanie siatki w oknie
        for x in range(0, self.window_size[0], PointCollection.grid_unit_size):
            pygame.draw.line(self.screen, self.axis_color2, (x, 0), (x, self.window_size[1]), 1)
            pygame.draw.line(self.screen, self.axis_color, (x, self.origin_y - 5), (x, self.origin_y + 5), 2)
        for y in range(0, self.window_size[1], PointCollection.grid_unit_size):
            pygame.draw.line(self.screen, self.axis_color2, (0, y), (self.window_size[0], y), 1)
            pygame.draw.line(self.screen, self.axis_color, (self.origin_x - 5, y), (self.origin_x + 5, y), 2)

        # Dodanie jednostki na siatkach
        TextObject.draw_text_object(self.screen, f"{PointCollection.grid_unit}",
                                    RelativePoint.calculate_point(self.window_size, PointCollection.grid_unit_size, -PointCollection.grid_unit_size),
                                    self.font, self.text_color)

        TextObject.draw_text_object(self.screen, f"{PointCollection.grid_unit}",
                                    RelativePoint.calculate_point(self.window_size, -PointCollection.grid_unit_size, PointCollection.grid_unit_size),
                                    self.font, self.text_color)

        # Podpisanie osi x i y
        TextObject.draw_text_object(self.screen, "x",
                                    RelativePoint.calculate_point(self.window_size,
                                                                  (self.window_size[0] // 2) - PointCollection.grid_unit_size,
                                                                  -1.5 * PointCollection.grid_unit_size),
                                    self.font2, self.text_color2)

        TextObject.draw_text_object(self.screen, "y",
                                    RelativePoint.calculate_point(self.window_size, -2 * PointCollection.grid_unit_size,
                                                                  (self.window_size[1] // 2) - (PointCollection.grid_unit_size // 2)),
                                    self.font2, self.text_color2)

        # Rysowanie otoczki
        convex_hull_draw(self.screen, PointCollection.points_convex_hull)

        # Rysowanie współrzędnych
        PointCollection.draw_points(self.screen, True) #self.tab_pressed)
