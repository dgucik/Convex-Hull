import pygame


class TextBox:
    def __init__(self, screen, window_size, rel_x_pos):
        self.screen = screen

        self.background_color = (255, 255, 255)
        self.border_color = (0, 0, 0)

        self.text_color = (0, 0, 0)

        self.font = pygame.freetype.Font(None, 24)

        self.text_box_width = 50
        self.text_box_height = 30

        self.text_box_x = (window_size[0] - self.text_box_width) // 2 + rel_x_pos
        self.text_box_y = (window_size[1] - self.text_box_height) // 2 - 60

        self.text_box_rect = pygame.Rect(self.text_box_x, self.text_box_y, self.text_box_width, self.text_box_height)

        self.input_text = ""
        self.text_box_active = False

    def get_text(self):
        txt = self.input_text
        self.input_text = ""
        return txt

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if self.text_box_active:
                if self.input_text == "" and event.key == pygame.K_MINUS:
                    self.input_text += "-"
                elif event.unicode.isnumeric():
                    self.input_text += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]

    def update(self, mouse_pos, mouse_click):
        if self.text_box_rect.collidepoint(mouse_pos) and mouse_click == 1:
            self.text_box_active = True
        elif mouse_click == 1:
            self.text_box_active = False

    def draw(self):
        pygame.draw.rect(self.screen, self.border_color, self.text_box_rect, 2)
        pygame.draw.rect(self.screen, self.background_color, self.text_box_rect)

        self.font.render_to(self.screen, (self.text_box_x + 5, self.text_box_y + 5), self.input_text[-3:], self.text_color)