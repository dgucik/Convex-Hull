class TextObject:
    @staticmethod
    def draw_text_object(surface, text, pos, font, color=(255, 255, 255)):
        """
        Rysuje obiekt tekstowy na podanej powierzchni.

        :param surface: Powierzchnia, na której ma zostać narysowany obiekt tekstowy.
        :param text: Tekst do wyświetlenia.
        :param pos: Pozycja, na której ma być wyśrodkowany obiekt tekstowy (x, y).
        :param font: Czcionka używana do wyrenderowania tekstu.
        :param color: Kolor tekstu (domyślnie biały).
        """
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = pos
        surface.blit(text_surface, text_rect)
