import pygame

BUTTON_STATES = ('RELEASED', 'PRESSED', 'ACTIVE', 'INACTIVE')


class Button:
    def __init__(self, x_pos, y_pos, width, height, txt):
        """
        Inicjalizuje obiekt przycisku.

        :param x_pos: Pozycja przycisku w osi x.
        :param y_pos: Pozycja przycisku w osi y.
        :param width: Szerokość przycisku.
        :param height: Wysokość przycisku.
        :param txt: Tekst wyświetlany na przycisku.
        """
        # Właściwości przycisku
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.text = txt
        self.border_width = 2

        # Kolory przycisków dla różnych stanów
        self.button_border_color = (0, 0, 0)
        self.button_released_color = (220, 220, 220)
        self.button_pressed_color = (180, 180, 180)
        self.button_active_color = (140, 140, 140)
        self.button_inactive_color = (100, 100, 100)

        # Stan przycisku
        self.button_state = BUTTON_STATES[0]

        # Utworzenie prostokąta dla przycisku
        self.button_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

        # Czcionka oraz położenie tekstu
        font = pygame.font.Font(None, 24)
        self.button_text = font.render(self.text, True, (0, 0, 0))
        self.button_text_x = ((self.width - self.button_text.get_width()) // 2)

    def update(self, mouse_pos, mouse_click):
        """
        Aktualizuje stan przycisku na podstawie pozycji myszy.

        :param mouse_pos: Pozycja myszy (x, y).
        :param mouse_click: Flaga wciśnięcia lewego przycisku myszy.
        :return: True, jeśli przycisk został wciśnięty, False w przeciwnym przypadku.
        """
        if self.button_state != BUTTON_STATES[3]:
            if self.button_rect.collidepoint(mouse_pos) & mouse_click:
                self.button_state = BUTTON_STATES[1]
                return True
            elif self.button_rect.collidepoint(mouse_pos):
                self.button_state = BUTTON_STATES[2]
            elif self.button_state == BUTTON_STATES[2]:
                self.button_state = BUTTON_STATES[0]

        return False

    def draw(self, surface):
        """
        Rysuje przycisk na podanej powierzchni.

        :param surface: Powierzchnia, na której ma zostać narysowany przycisk.
        """
        # Rysowanie przycisków w zależności od stanu
        if self.button_state == 'RELEASED':
            pygame.draw.rect(surface, self.button_released_color, self.button_rect)
        elif self.button_state == 'PRESSED':
            pygame.draw.rect(surface, self.button_pressed_color, self.button_rect)
        elif self.button_state == 'ACTIVE':
            pygame.draw.rect(surface, self.button_active_color, self.button_rect)
        elif self.button_state == 'INACTIVE':
            pygame.draw.rect(surface, self.button_inactive_color, self.button_rect)

        # Rysowanie obrazmowania przycisku
        pygame.draw.rect(surface, self.button_border_color, (self.x_pos, self.y_pos, self.width, self.height),
                         self.border_width)

        # Umieszczenie przycisku na pozycji docelowej w oknie
        surface.blit(self.button_text, (self.button_text_x + self.x_pos, self.button_rect.y + 7))
