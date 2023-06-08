import pygame
from components.button import Button
from containters.point_collection import PointCollection
from components.text_box import TextBox
from components.text_object import TextObject


class SubWindow:
    def __init__(self, main_window_size):
        """
        Reprezentuje podokno aplikacji.

        :param main_window_size: Rozmiar głównego okna w pikselach (szerokość, wysokość).
        """
        # Ustawienie szerokości podokna, pozycji oraz grubości obramowania
        self.main_window_size = main_window_size
        self.sub_window_size = (main_window_size[0] // 4, main_window_size[1] // 4)
        self.position = (main_window_size[0] - self.sub_window_size[0], main_window_size[1] - self.sub_window_size[1])
        self.border_width = 1

        # Kolor tła okna oraz obramowania
        self.background_color = (240, 240, 240)
        self.border_color = (0, 0, 0)

        # Utworzenie podokna aplikacji
        self.screen = pygame.Surface(self.sub_window_size)

        # Wymiary przycisków
        self.button_width = self.sub_window_size[0] - (self.sub_window_size[0] // 3)
        self.button_height = self.sub_window_size[1] // 7

        # Położenie przycisku w osi x
        self.button_x = (self.sub_window_size[0] - self.button_width) // 2

        # Utworzenie przycisków
        self.add_button_y = (self.sub_window_size[1] - self.button_height) // 2
        self.add_button = Button(self.button_x, self.add_button_y, self.button_width, self.button_height, "Dodaj punkt")

        self.start_button_y = ((self.sub_window_size[1] - self.button_height) // 2) + 40
        self.start_button = Button(self.button_x, self.start_button_y, self.button_width, self.button_height, "Otoczka")

        self.restart_button_y = ((self.sub_window_size[1] - self.button_height) // 2) + 80
        self.restart_button = Button(self.button_x, self.restart_button_y, self.button_width, self.button_height,
                                     "Wyczyść")

        # Utworzenie atrybutów reprezentujących zdarzenia
        self.mouse_pos = (0, 0)
        self.mouse_click = False
        self.space_active = False

        # Położenie napisów w podoknie
        self.text_object_x_pos = 110
        self.text_object_y_pos = (self.sub_window_size[1] - 30) // 2 - 45

        self.text_box_xcor_x_pos = -60
        self.text_box_xcor = TextBox(self.screen, self.sub_window_size, self.text_box_xcor_x_pos) # Obiekt dla współrzędnych x

        self.text_box_ycor_x_pos = 60
        self.text_box_ycor = TextBox(self.screen, self.sub_window_size, self.text_box_ycor_x_pos) # Obiekt dla współrzędncyh y

    def handle_events(self, event):
        """
        Obsługuje zdarzenia Pygame.

        :param event: Zdarzenie Pygame.
        """
        # Pobierz pozycje kursora
        self.mouse_pos = (pygame.mouse.get_pos()[0] - self.position[0], pygame.mouse.get_pos()[1] - self.position[1])

        # Pobierz stan przycisku spacji
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.space_active = not self.space_active

        # Jeśli spacja nie jest aktywna to sprawdź czy LPM jest aktywny
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.space_active == False:
            self.mouse_click = True
        else:
            self.mouse_click = False

        # Obsłuż zdarzenia przycisków jeśli spacja nie jest aktywna
        if not self.space_active:
            self.text_box_xcor.handle_events(event)
            self.text_box_ycor.handle_events(event)

    def update(self):
        """
        Aktualizuje stan podokna.
        """
        if not self.space_active:
            # Pobierz stan przycisków podokna
            add_button_pressed = self.add_button.update(self.mouse_pos, self.mouse_click)
            start_button_pressed = self.start_button.update(self.mouse_pos, self.mouse_click)
            restart_button_pressed = self.restart_button.update(self.mouse_pos, self.mouse_click)

            # Wprowadzanie współrzędnych dla punktów
            self.text_box_xcor.update(self.mouse_pos, self.mouse_click)
            self.text_box_ycor.update(self.mouse_pos, self.mouse_click)

            # Obsługa przycisków w podoknie
            if add_button_pressed:
                x = self.text_box_xcor.input_text
                y = self.text_box_ycor.input_text
                if x != "" and y != "" and x != "-" and y != "-":
                    PointCollection.add_point((int(x), int(y)))
                    self.text_box_xcor.clear_text()
                    self.text_box_ycor.clear_text()
            if start_button_pressed:
                pass
            if restart_button_pressed:
                PointCollection.clear_array()
                PointCollection.grid_unit = 1

    def draw(self, surface):
        """
        Rysuje podokno na powierzchni.

        :param surface: Powierzchnia, na której rysowane jest podokno.
        """
        if not self.space_active:
            # Wypełnienie tła oraz rysowanie obramowania
            self.screen.fill(self.background_color)
            pygame.draw.rect(self.screen, self.border_color, (0, 0, self.sub_window_size[0], self.sub_window_size[1]),
                             self.border_width)

            # Rysowanie przycisków
            self.add_button.draw(self.screen)
            self.start_button.draw(self.screen)
            self.restart_button.draw(self.screen)

            # Rysowanie wprowadzanych współrzędnych
            TextObject.draw_text_object(self.screen, "x = ", (self.text_object_x_pos + self.text_box_xcor_x_pos , self.text_object_y_pos), pygame.font.SysFont("arial", 18, True, False), (0, 0, 0))
            self.text_box_xcor.draw()

            TextObject.draw_text_object(self.screen, "y = ", (self.text_object_x_pos + self.text_box_ycor_x_pos, self.text_object_y_pos), pygame.font.SysFont("arial", 18, True, False), (0, 0, 0))
            self.text_box_ycor.draw()

            # Umieszczenie podokna na pozycji docelowej
            surface.blit(self.screen, self.position)
