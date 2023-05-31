import pygame

BUTTON_STATES = ('RELEASED', 'PRESSED', 'ACTIVE', 'INACTIVE')


class Button:
    def __init__(self, x_pos, y_pos, width, height, txt):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.text = txt
        self.border_width = 2

        self.button_border_color = (0, 0, 0)
        self.button_released_color = (220, 220, 220)
        self.button_pressed_color = (180, 180, 180)
        self.button_active_color = (140, 140, 140)
        self.button_inactive_color = (100, 100, 100)

        self.button_state = BUTTON_STATES[0]

        self.button_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

        font = pygame.font.Font(None, 24)
        self.button_text = font.render(self.text, True, (0, 0, 0))
        self.button_text_x = ((self.width - self.button_text.get_width()) // 2)

    def update(self, mouse_pos, mouse_click):
        if self.button_state != BUTTON_STATES[3]:
            if self.button_rect.collidepoint(mouse_pos) & mouse_click:
                self.button_state = BUTTON_STATES[1]
            elif self.button_rect.collidepoint(mouse_pos):
                self.button_state = BUTTON_STATES[2]
            elif self.button_state == BUTTON_STATES[2]:
                self.button_state = BUTTON_STATES[0]

    def draw(self, surface):
        if self.button_state == 'RELEASED':
            pygame.draw.rect(surface, self.button_released_color, self.button_rect)
        elif self.button_state == 'PRESSED':
            pygame.draw.rect(surface, self.button_pressed_color, self.button_rect)
        elif self.button_state == 'ACTIVE':
            pygame.draw.rect(surface, self.button_active_color, self.button_rect)
        elif self.button_state == 'INACTIVE':
            pygame.draw.rect(surface, self.button_inactive_color, self.button_rect)

        pygame.draw.rect(surface, self.button_border_color, (self.x_pos, self.y_pos, self.width, self.height),
                         self.border_width)
        surface.blit(self.button_text, (self.button_text_x + self.x_pos, self.button_rect.y + 7))
