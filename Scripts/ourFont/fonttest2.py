
import pygame
import sys
sys.path.append('/Users/bmors/Documents/CSC 465/project_scripts/Application/ourFont')
from ourFont import ourFont


# Pygame window setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Number Keypad Example')

# Our font setup
font_folder = '/Users/bmors/Documents/CSC 465/project_scripts/Application/ourFont'
font = ourFont(font_folder)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            font.handle_event(event)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 100 <= pos[0] < 200 and 100 <= pos[1] < 200:
                    print('1')
                elif 200 <= pos[0] < 300 and 100 <= pos[1] < 200:
                    print('2')
                elif 300 <= pos[0] < 400 and 100 <= pos[1] < 200:
                    print('3')
                elif 100 <= pos[0] < 200 and 200 <= pos[1] < 300:
                    print('4')
                elif 200 <= pos[0] < 300 and 200 <= pos[1] < 300:
                    print('5')
                elif 300 <= pos[0] < 400 and 200 <= pos[1] < 300:
                    print('6')
                elif 100 <= pos[0] < 200 and 300 <= pos[1] < 400:
                    print('7')
                elif 200 <= pos[0] < 300 and 300 <= pos[1] < 400:
                    print('8')
                elif 300 <= pos[0] < 400 and 300 <= pos[1] < 400:
                    print('9')

    screen.fill((255, 255, 255))
    font.render_text('1', screen, 110, 110)
    font.render_text('2', screen, 210, 110)
    font.render_text('3', screen, 310, 110)
    font.render_text('4', screen, 110, 210)
    font.render_text('5', screen, 210, 210)
    font.render_text('6', screen, 310, 210)
    font.render_text('7', screen, 110, 310)
    font.render_text('8', screen, 210, 310)
    font.render_text('9', screen, 310, 310)
    pygame.display.flip()

pygame.quit()
