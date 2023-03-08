import pygame
import sys
import os
MENU_SCREEN = "/home/bdm/SoundViz/Application/Driver/"
sys.path.append('/home/bdm/SoundViz/Application/Driver/MenuSurface')
sys.path.append('/home/bdm/SoundViz/Application/Driver/LoadingSurface')
from MenuSurface import MenuSurface
from LoadingSurface import LoadingSurface


# Initialize Pygame
pygame.init()

# Set the screen size
screen_size = (800, 450)
screen = pygame.display.set_mode(screen_size)


# Create a loading screen
# loading_surface = LoadingSurface(screen_size)

# Load resources here...
bg_image_path = os.path.abspath("/home/bdm/SoundViz/Application/Driver/MenuSurface/menu_bg.png")
bg_image = pygame.image.load(bg_image_path).convert_alpha()
logo_image_path = os.path.abspath("/home/bdm/SoundViz/Application/Driver/MenuSurface/menu_logo.png")
logo_image = pygame.image.load(logo_image_path).convert_alpha()

# Set up the game loop
loading_progress = 0
menu_surface = MenuSurface(screen_size)
loading_surface = LoadingSurface(screen_size)
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the loading progress
    loading_progress += 0.0025
    if loading_progress >= 1.0:
        loading_progress = 1.0

    # Render the loading screen
    loading_surface.render(loading_progress)

    # Update the display
    screen.blit(loading_surface, (0, 0))
    pygame.display.update()

    # If loading is complete, render the menu screen
    if loading_progress >= 1.0:
        menu_surface.render()
        screen.blit(menu_surface, (0, 0))
        pygame.display.update()
        running = False


# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if menu_surface.button_rect.collidepoint(event.pos):
                running = False

    # Render the menu
    menu_surface.render()

    # Update the display
    screen.blit(menu_surface, (0, 0))
    pygame.display.update()

# Quit Pygame
pygame.quit()
