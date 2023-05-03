import pygame


# Initialize pygame
pygame.init()

# Set the size of the window
screen = pygame.display.set_mode((1000, 700))

#class ManualCalibration:
# Set the font and font size
font = pygame.font.SysFont("Arial", 20)


# Set the text for the input fields
Title = font.render("Manual Calibration", True, (0, 0, 0))
text1 = font.render("A: ", True, (0, 0, 0))
text2 = font.render("B: ", True, (0, 0, 0))
text3 = font.render("C: ", True, (0, 0, 0))

# Set the text for the button
gobutton_text = font.render("GO", True, (0, 0, 0))


# Set the rectangle for the input fields
input_rect1 = pygame.Rect(175, 50, 100, 25)
input_rect2 = pygame.Rect(175, 100, 100, 25)
input_rect3 = pygame.Rect(175, 150, 100, 25)

# Set the rectangle for the button
gobutton_rect = pygame.Rect(150, 200, 100, 25)

# Set the default input values
param1 = ""
param2 = ""
param3 = ""

# Set the main loop for the program
running = True
while running:
    screen.fill(255)
    # Check for events
    for event in pygame.event.get():

        # Quit the program when the user closes the window
        if event.type == pygame.QUIT:
            running = False

        # Check for input from the user
        if event.type == pygame.KEYDOWN:

            # Check if the input field is active
            if input_rect1.collidepoint(pygame.mouse.get_pos()):
                if event.key == pygame.K_BACKSPACE:
                    param1 = param1[:-1]
                else:
                    param1 += event.unicode
            elif input_rect2.collidepoint(pygame.mouse.get_pos()):
                if event.key == pygame.K_BACKSPACE:
                    param2 = param2[:-1]
                else:
                    param2 += event.unicode
            elif input_rect3.collidepoint(pygame.mouse.get_pos()):
                if event.key == pygame.K_BACKSPACE:
                    param3 = param3[:-1]
                else:
                    param3 += event.unicode

        # Check for button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gobutton_rect.collidepoint(pygame.mouse.get_pos()):
                print("Parameters:", param1, param2, param3)

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw the input fields
    pygame.draw.rect(screen, (0, 0, 0), input_rect1, 1)
    pygame.draw.rect(screen, (0, 0, 0), input_rect2, 1)
    pygame.draw.rect(screen, (0, 0, 0), input_rect3, 1)

    # Draw the button
    pygame.draw.rect(screen, (0, 0, 0), gobutton_rect, 1)

    # Blit the text onto the screen
    screen.blit(Title, (55, 15))
    screen.blit(text1, (130, 50))
    screen.blit(text2, (130, 100))
    screen.blit(text3, (130, 150))
    screen.blit(gobutton_text, (175, 205))

    # Blit the user's input onto the screen
    input1 = font.render(param1, True, (0, 0, 0))
    screen.blit(input1, (175, 50))

    input2 = font.render(param2, True, (0, 0, 0))
    screen.blit(input2, (175, 100))

    input3 = font.render(param3, True, (0, 0, 0))
    screen.blit(input3, (175, 150))

    # Update the display
    pygame.display.update()

pygame.quit()
