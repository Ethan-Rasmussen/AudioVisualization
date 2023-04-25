import os
import pygame
import sys

class LoadingSurface(pygame.Surface):
    def __init__(self, size, Folder = ''):
        self.AppHomeFolder = Folder
        currentDir = self.AppHomeFolder + '/LoadingSurface'
        sys.path.append(currentDir)
        # Set up the game loop
        loading_progress = 0
        super().__init__(size)
        self.bg_color = (50, 50, 50)
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render("Loading...", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=self.get_rect().center)

    def render(self, progress):
        # Fill the surface with the background color
        self.fill(self.bg_color)
        
        # Draw the progress bar
        bar_width = self.get_width() - 40
        bar_height = 20
        bar_rect = pygame.Rect(20, self.get_height() - 40, bar_width, bar_height)
        progress_rect = pygame.Rect(bar_rect.left, bar_rect.top, bar_width * (progress), bar_height)
        pygame.draw.rect(self, (255, 255, 255), bar_rect, 2)
        pygame.draw.rect(self, (255, 255, 255), progress_rect)
        
        # Draw the "Loading..." text
        self.blit(self.text, self.text_rect)
