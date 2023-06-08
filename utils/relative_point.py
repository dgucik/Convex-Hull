class RelativePoint:
    @staticmethod
    def calculate_point(reference_point, x, y):
        """
        Oblicza punkt na układzie współrzędnych względem konkretnego punktu referencyjnego.

        :param reference_point: Punkt referencyjny w formacie (x_ref, y_ref).
        :param x: Wartość współrzędnej x.
        :param y: Wartość współrzędnej y.
        :return: Obliczony punkt w formacie (x_abs, y_abs).
        """
        x_abs = (reference_point[0] // 2) + x
        y_abs = (reference_point[1] // 2) - y
        return x_abs, y_abs
