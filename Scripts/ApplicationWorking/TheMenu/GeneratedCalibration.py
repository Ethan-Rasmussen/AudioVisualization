import pygame


# Initialize pygame
pygame.init()

# Set the size of the window
screen = pygame.display.set_mode((1000, 700))

#class ManualCalibration:
# Set the font and font size
font = pygame.font.SysFont("Arial", 20)


# Set the text for the input fields
text1 = font.render("Parameter A: ", True, (0, 0, 0))
text2 = font.render("Parameter B: ", True, (0, 0, 0))
text3 = font.render("Parameter C: ", True, (0, 0, 0))

# Set the text for the button
gobutton_text = font.render("GO", True, (0, 0, 0))
newbutton_text = font.render("New Parameters", True, (0, 0, 0))


# Set the rectangle for the input fields
#input_rect1 = pygame.Rect(150, 50, 100, 25)
input_rect2 = pygame.Rect(150, 100, 100, 25)
input_rect3 = pygame.Rect(150, 150, 100, 25)

# Set the rectangle for the button
gobutton_rect = pygame.Rect(150, 200, 100, 25)
newbutton_rect = pygame.Rect(275, 200, 150, 25)

# Set the default input values
param1 = "1"
param2 = "2"
param3 = "3"

# Set the main loop for the program
running = True
while running:
    screen.fill(255)
    # Check for events
    for event in pygame.event.get():

        # Quit the program when the user closes the window
        if event.type == pygame.QUIT:
            running = False

        # Check for button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gobutton_rect.collidepoint(pygame.mouse.get_pos()):
                print("Parameters:", param1, param2, param3)
                
        # Process New Parameters
        if event.type == pygame.MOUSEBUTTONDOWN:
            if newbutton_rect.collidepoint(pygame.mouse.get_pos()):
                param1 = param1 + "NEW"
                param2 = param2 + "NEW"
                param3 = param3 + "NEW"

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw the button
    pygame.draw.rect(screen, (0, 0, 0), gobutton_rect, 1)
    pygame.draw.rect(screen, (0, 0, 0), newbutton_rect, 1)

    # Blit the text onto the screen
    screen.blit(text1, (50, 50))
    screen.blit(text2, (50, 100))
    screen.blit(text3, (50, 150))
    screen.blit(gobutton_text, (175, 205))
    screen.blit(newbutton_text, (275, 205))

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

