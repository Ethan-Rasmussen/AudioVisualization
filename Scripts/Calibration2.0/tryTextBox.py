import pygame
from TextBox import TextBox
pygame.init()
clock = pygame.time.Clock()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Multiple Text Boxes")

# Create a list of text boxes
text_boxes = [
    TextBox(100, 100, 200, 30, 20),
    TextBox(300, 200, 200, 30, 20),
    TextBox(200, 300, 200, 30, 20)
]

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the screen
    screen.fill((0, 0, 0))
    for text_box in text_boxes:
        text_box.draw(screen)

    # Check if any text boxes are clicked and start their respective loops
    for i, text_box in enumerate(text_boxes):
        if pygame.mouse.get_pressed()[0] and text_box.rect.collidepoint(pygame.mouse.get_pos()):
            text_box.run(screen)

    pygame.display.flip()
    clock.tick(30)