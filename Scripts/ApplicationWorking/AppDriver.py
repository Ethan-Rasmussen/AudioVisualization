'''
This is going to be the final format we have to start going with.

The good news is, there is no more worry about aligning the proper address
for the folers within this one, nor do you need to change anything about
this one for it to work straight away after a code download.

At least, if all goes to plan, anything that you import using the new import format,
should actually get imported.

That is why we want to be able to define everything as a class, so that we can import it
and have it work right away, while having the controlled file scope of it being in its own folder.
The beauty of the this is that when you make a new screen/module/program whatever term you like,
you can just toss you folder in there and know that everything works since you followed this
importing format, and the foler you are trying to add, will go insider the [Application] folder, somewhere.
'''



import pygame
import sys
import os
AppHomeFolder = os.getcwd()
print(AppHomeFolder)
sys.path.append(AppHomeFolder + '/MenuSurface')
sys.path.append(AppHomeFolder + '/LoadingSurface')
sys.path.append(AppHomeFolder + '/TheMenu')
from MenuSurface import MenuSurface
from LoadingSurface import LoadingSurface
from TheMenu import run_sound_visualization_menu
import time


# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()
max_fps = 180

# Set the screen size
screen_size = (800, 450)
screen = pygame.display.set_mode(screen_size)


# Create a loading screen
# loading_surface = LoadingSurface(screen_size)

# Load resources here...
bg_image_path = AppHomeFolder + '/MenuSurface/menu_bg.png'
bg_image = pygame.image.load(bg_image_path).convert_alpha()
logo_image_path = AppHomeFolder + '/MenuSurface//menu_logo.png'
logo_image = pygame.image.load(logo_image_path).convert_alpha()

# Set up the game loop
loading_progress = 0
menu_surface = MenuSurface(screen_size, AppHomeFolder)
loading_surface = LoadingSurface(screen_size, AppHomeFolder)
running = True
while running:
    clock.tick(max_fps)
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
                # Render the menu
                run_sound_visualization_menu(AppHomeFolder)
                #menu_surface.render()
                #menu_surface.run_menu_surface()
                running = False

# Render the menu
#menu_surface.render()
#MenuSurface.run_menu_surface(MenuSurface, AppHomeFolder)

# Update the display
#screen.blit(menu_surface, (0, 0))
pygame.display.update()


# Quit Pygame
pygame.quit()



