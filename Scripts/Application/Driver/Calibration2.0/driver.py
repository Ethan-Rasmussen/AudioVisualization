import pygame

# Initialize pygame
pygame.init()

# Set the size of the window
screen = pygame.display.set_mode((1000, 700))

# Set the font and font size
font = pygame.font.SysFont("Arial", 20)


button_text = font.render("GO", True, (0, 0, 0))
# Set the rectangle for the button
button_rect = pygame.Rect(150, 200, 100, 25)


screen.fill((255,255,255))

    # Set the main loop for the program
running = True
while running:

    for event in pygame.event.get():

        # Quit the program when the user closes the window
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Parameters:", param1, param2, param3)

    screen.fill((255,255,255))

    # Update the display
    pygame.display.update()

pygame.quit()