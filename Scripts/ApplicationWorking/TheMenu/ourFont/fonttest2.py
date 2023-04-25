import pygame
import sys
import os


fontFolder = os.getcwd()
#-------------------------------------------------------------------------------#|
#PROPER FORMAT FOR IMPORTING A FILE(from within 'Application' folder somewhere) #|
############################################################################### #|
currentDirectory = ''                                              #|
sys.path.append(fontFolder)                                        #|
currentDirectory = fontFolder + '/ourFont'                    #|
from ourFont import ourFont
sys.path.append(currentDirectory)                                  #|
#-------------------------------------------------------------------------------#|

# Pygame window setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Number Keypad Example')

# Our font setup
font_folder = fontFolder
font = ourFont(font_folder)

# Key positions and dimensions
key_pad_left = 100
key_pad_top = 300
key_width = 40
key_height = 40
key_border = 5

key_color = (50, 50, 50)  # Define key color as red (R, G, B values)


screen.fill((255, 255, 255))

def showNumberPad(screen, key_pad_left, key_pad_top, key_width, key_height, key_border, key_color, input_text):
    # Render the input text above the keypad
    input_rect = font.render_text(input_text, screen, screen_width // 2, key_pad_top - 50)

    for i in range(1, 10):
        # Draw the key box
        key_rect = pygame.Rect(key_pad_left + ((i - 1) % 3) * (key_width + key_border),
                               key_pad_top + ((i - 1) // 3) * (key_height + key_border),
                               key_width, key_height)
        pygame.draw.rect(screen, key_color, key_rect)

        # Render the key text
        font.render_text(str(i), screen, key_rect.centerx-6, key_rect.centery-10.5)

    #pygame.display.update([input_rect, screen.blit(screen, (0, 0))])  # Update only the changed regions of the screen




# Main loop
input_text = ''  # Initialize the input text to an empty string
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            font.handle_event(event)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if key_pad_left <= pos[0] < key_pad_left + key_width and key_pad_top <= pos[1] < key_pad_top + key_height:
                    input_text += '1'
                elif key_pad_left + key_width + key_border <= pos[0] < key_pad_left + 2 * key_width + key_border and key_pad_top <= pos[1] < key_pad_top + key_height:
                    input_text += '2'
                elif key_pad_left + 2 * (key_width + key_border) <= pos[0] < key_pad_left + 3 * key_width + 2 * key_border and key_pad_top <= pos[1] < key_pad_top + key_height:
                    input_text += '3'
                elif key_pad_left <= pos[0] < key_pad_left + key_width and key_pad_top + key_height + key_border <= pos[1] < key_pad_top + 2 * key_height + key_border:
                    input_text += '4'
                elif key_pad_left + key_width + key_border <= pos[0] < key_pad_left + 2 * key_width + key_border and key_pad_top + key_height + key_border <= pos[1] < key_pad_top + 2 * key_height + key_border:
                    input_text += '5'
                elif key_pad_left + 2 * (key_width + key_border) <= pos[0] < key_pad_left + 3 * key_width + 2 * key_border and key_pad_top + key_height + key_border <= pos[1] < key_pad_top + 2 * key_height + key_border:
                    input_text += '6'
                elif key_pad_left <= pos[0] < key_pad_left + key_width and key_pad_top + 2 * (key_height + key_border) <= pos[1] < key_pad_top + 3 * key_height + 2 * key_border:
                    input_text += '7'
                elif key_pad_left + key_width + key_border <= pos[0] < key_pad_left + 2 * key_width + key_border and key_pad_top + 2 * (key_height + key_border) <= pos[1] < key_pad_top + 3 * key_height + 2 * key_border:
                    input_text += '8'
                elif key_pad_left + 2 * (key_width + key_border) <= pos[0] < key_pad_left + 3 * key_width + 2 * key_border and key_pad_top + 2 * (key_height + key_border) <= pos[1] < key_pad_top + 3 * key_height + 2 * key_border:
                    input_text += '9'
                elif key_pad_left + key_width + key_border <= pos[0] < key_pad_left + 2 * key_width + key_border and key_pad_top + 3 * (key_height + key_border) <= pos[1] < key_pad_top + 4 * key_height + 3 * key_border:
                    input_text += '0'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1] # Delete the last character from the input text


                                    
                    

    screen.fill((255, 255, 255))
    font.render_text(input_text, screen, (screen_width // 2), key_pad_top - 50 - 10.5)  # Display input text above the keypad
    showNumberPad(screen, key_pad_left, key_pad_top, key_width, key_height, key_border, key_color, input_text)
    pygame.display.flip()

pygame.quit()

