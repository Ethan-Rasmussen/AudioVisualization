import os
import pygame

class MenuSurface(pygame.Surface):
    def __init__(self, size):
        super().__init__(size)
        bg_image_path = os.path.abspath("/home/bdm/SoundViz/Application/Driver/MenuSurface/menu_bg.png")
        logo_image_path = os.path.abspath("/home/bdm/SoundViz/Application/Driver/MenuSurface/menu_logo.png")
        self.bg_image = pygame.image.load(bg_image_path).convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, size)
#         self.logo_image = pygame.image.load("menu_logo.png").convert_alpha()
        self.font = pygame.font.Font(None, 30)
        self.text1 = self.font.render("Sound Visualization Application", True, (12, 80, 12))
        self.button_rect = pygame.Rect(size[0] // 2 - 100, 450/2-37.5, 200, 75)
        self.button_font = pygame.font.Font(None, 38)
        self.button_text = self.button_font.render("Start", True, (20, 20, 20))
        self.button_text_rect = self.button_text.get_rect()
        self.button_text_rect.centerx = self.button_rect.centerx
        self.button_text_rect.centery = self.button_rect.centery

    def render(self):
        self.blit(self.bg_image, (0, 0))
        self.blit(self.text1, self.text1.get_rect(centerx=self.get_width() // 2, top=10))
        pygame.draw.rect(self, (255, 255, 20), self.button_rect, 2)
        pygame.draw.rect(self, (255, 255, 20), self.button_rect)
        self.blit(self.button_text, self.button_text_rect)