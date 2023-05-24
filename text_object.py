class TextObject:
    @staticmethod
    def draw_text_object(surface, text, pos, font, color=(255, 255, 255)):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = pos
        surface.blit(text_surface, text_rect)
