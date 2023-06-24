import pygame
from pygame import freetype


class TextBox:
    def __init__(self, screen, window_size, rel_x_pos):
        """
        Inicjalizuje obiekt TextBox.

        :param screen: Powierzchnia, na której ma zostać narysowany TextBox.
        :param window_size: Rozmiar okna głównego (szerokość, wysokość).
        :param rel_x_pos: Relatywna pozycja w osi x TextBoxu w stosunku do środka okna głównego.
        """
        self.screen = screen

        # Kolor tła, obramowania oraz wprowadzanego tekstu
        self.background_color = (255, 255, 255)
        self.border_color = (0, 0, 0)
        self.text_color = (0, 0, 0)

        # Czcionka
        self.font = freetype.Font(None, 24)

        # Wymiary obszaru
        self.text_box_width = 50
        self.text_box_height = 30

        # Położenie tekstu
        self.text_box_x = (window_size[0] - self.text_box_width) // 2 + rel_x_pos
        self.text_box_y = (window_size[1] - self.text_box_height) // 2 - 60

        # Utworzenie prostokąta dla tekstu
        self.text_box_rect = pygame.Rect(self.text_box_x, self.text_box_y, self.text_box_width, self.text_box_height)

        # Utworzenie atrybutów reprezentujących zdarzenia oraz wprowadzane dane
        self.input_text = ""
        self.text_box_active = False

    def clear_text(self):
        """
        Czyści tekst wprowadzony w TextBoxie.
        """
        self.input_text = ""

    def handle_events(self, event):
        """
        Obsługuje zdarzenia Pygame.

        :param event: Zdarzenie Pygame.
        """
        if event.type == pygame.KEYDOWN:
            if self.text_box_active:
                if self.input_text == "" and event.key == pygame.K_MINUS:
                    self.input_text += "-"
                elif event.unicode.isnumeric():
                    if event.unicode == '0':
                        if self.input_text != "-" and self.input_text != "0":
                            self.input_text += event.unicode
                    elif self.input_text != '0':
                        self.input_text += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]

    def update(self, mouse_pos, mouse_click):
        """
        Aktualizuje stan TextBoxu na podstawie pozycji kursora myszy i kliknięcia.

        :param mouse_pos: Pozycja kursora myszy (x, y).
        :param mouse_click: Stan kliknięcia myszy (0 - niekliknięte, 1 - kliknięte).
        """
        if self.text_box_rect.collidepoint(mouse_pos) and mouse_click == 1:
            self.text_box_active = True
        elif mouse_click == 1:
            self.text_box_active = False

    def draw(self):
        """
        Rysuje TextBox na powierzchni.
        """
        pygame.draw.rect(self.screen, self.background_color, self.text_box_rect)
        if self.text_box_active:
            pygame.draw.rect(self.screen, self.border_color, self.text_box_rect, 2)

        self.font.render_to(self.screen, (self.text_box_x + 5, self.text_box_y + 5), self.input_text[-3:], self.text_color)