import pygame

from utils.relative_point import RelativePoint
from components.text_object import TextObject


class PointCollection:
    points = [] # Tablica przechowująca wszystkie dodane punkty
    grid_unit = 1 # Wartość siatki współrzędnych
    grid_unit_size = 20 # Ilość pikseli na jeden krok

    @staticmethod
    def add_point(point):
        """
        Dodaje punkt do kolekcji punktów.

        :param point: Punkt w formacie (x, y).
        """
        PointCollection.points.append(point)

    @staticmethod
    def clear_array():
        """
        Czyści kolekcję punktów.
        """
        PointCollection.points.clear()

    @staticmethod
    def draw_points(screen, show_cords = False):
        """
        Rysuje wszystkie punkty na ekranie.

        :param screen: Obiekt ekranu pygame.
        :param show_coords: Określa, czy wyświetlać współrzędne punktów.
        """
        for point in PointCollection.points:
            # Obliczenie położenia punktów
            x_pos = (point[0] * PointCollection.grid_unit_size) // PointCollection.grid_unit
            y_pos = (point[1] * PointCollection.grid_unit_size) // PointCollection.grid_unit

            # Rysowanie punktów
            pygame.draw.circle(screen, (255, 0, 0), RelativePoint.calculate_point(screen.get_size(), x_pos, y_pos), 5)

            # Wyświetlenie współrzędnych wszystkich punktów
            if show_cords:
                TextObject.draw_text_object(screen, f"({point[0]}, {point[1]})", RelativePoint.calculate_point(screen.get_size(), x_pos, y_pos + 5),
                                            pygame.font.SysFont("arial", 14, False, False), (0, 0, 0))