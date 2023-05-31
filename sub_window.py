import pygame
from button import Button


class SubWindow:
    def __init__(self, window_size):
        self.sub_window_size = (window_size[0] // 4, window_size[1] // 4)
        self.position = (window_size[0] - self.sub_window_size[0], window_size[1] - self.sub_window_size[1])
        self.border_width = 1

        self.background_color = (240, 240, 240)
        self.border_color = (0, 0, 0)

        self.screen = pygame.Surface(self.sub_window_size)

        self.button_width = self.sub_window_size[0] - (self.sub_window_size[0] // 3)
        self.button_height = self.sub_window_size[1] // 7
        self.button_x = (self.sub_window_size[0] - self.button_width) // 2

        self.add_button_y = (self.sub_window_size[1] - self.button_height) // 2
        self.add_button = Button(self.button_x, self.add_button_y, self.button_width, self.button_height, "Dodaj punkt")

        self.start_button_y = ((self.sub_window_size[1] - self.button_height) // 2) + 40
        self.start_button = Button(self.button_x, self.start_button_y, self.button_width, self.button_height, "Start")

        self.restart_button_y = ((self.sub_window_size[1] - self.button_height) // 2) + 80
        self.restart_button = Button(self.button_x, self.restart_button_y, self.button_width, self.button_height,
                                     "Restart")

        # steering
        self.mouse_pos = (0, 0)
        self.mouse_click = False
        self.space_active = False

    def handle_events(self, event):
        self.mouse_pos = (pygame.mouse.get_pos()[0] - self.position[0], pygame.mouse.get_pos()[1] - self.position[1])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.space_active = not self.space_active

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.space_active == False:
            self.mouse_click = True
        else:
            self.mouse_click = False

    def update(self):
        self.add_button.update(self.mouse_pos, self.mouse_click)
        self.start_button.update(self.mouse_pos, self.mouse_click)
        self.restart_button.update(self.mouse_pos, self.mouse_click)

    def draw(self, surface):
        if self.space_active == False:
            self.screen.fill(self.background_color)
            pygame.draw.rect(self.screen, self.border_color, (0, 0, self.sub_window_size[0], self.sub_window_size[1]),
                             self.border_width)

            self.add_button.draw(self.screen)
            self.start_button.draw(self.screen)
            self.restart_button.draw(self.screen)

            surface.blit(self.screen, self.position)
