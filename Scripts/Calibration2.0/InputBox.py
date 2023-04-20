import pygame
import sys
from ourFont import ourFont
class InputBox:
    def __init__(self, rect, text="", color_active='lightskyblue3', color_inactive='gray15', font_name='RobotoCondensed-Regular.ttf', font_size=20):
        self.rect = pygame.Rect(rect)
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.font_name = font_name
        self.font_size = font_size
        font_name = 'RobotoCondensed-Regular.ttf'
        font_size = 20
#         # Load font
#         self.font = pygame.font.Font(font_name, font_size)
#         self.text = text
#         self.txt_surface = self.font.render(self.text, True, self.color_inactive)
#         self.active = False
        
        # Initialize pygame font module
        pygame.font.init()
        
#         # Load font
#         try:
#             self.font = pygame.font.Font(self.font_name, self.font_size)
#         except pygame.error as e:
#             print(f"Error loading font: {e}")


    def handle_event(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            #self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        # Re-render the text.
        #self.txt_surface = self.font.render(self.text, True, self.color_active)
        #return ourFont.render_text(self, self.text, screen, self.rect.x+5, self.rect.y+5)

#     def draw(self, screen):
#         self.txt_surface = self.font.render(self.text, True, self.color_inactive)
#         #Blit the text.
#         screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))        # Blit the rect.
#         pygame.draw.rect(screen, self.color_active, self.rect, 2)
