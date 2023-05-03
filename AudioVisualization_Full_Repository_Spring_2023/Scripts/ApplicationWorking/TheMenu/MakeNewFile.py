import pygame
import sys

class MakeNewFile:
    def __init__(self, screen, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.image.load('main_menu_bg.png').convert()
        self.font = pygame.font.SysFont(None, 30)
        self.clock = pygame.time.Clock()

        # Initialize input box variables
        self.input_box = pygame.Rect(250, 200, 300, 40)
        self.input_text = ''
        self.is_input_active = False

        # Initialize button variables
        self.return_button = pygame.Rect(775, 0, 25, 25)
        self.make_button = pygame.Rect(450, 250, 150, 50)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        text = self.font.render('Enter File Name:', True, (255, 255, 255))
        self.screen.blit(text, (150, 150))


        # Draw input box
        pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)
        text_surface = self.font.render(self.input_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))

        # Draw buttons
        make_text = self.font.render("Make", True, (255, 255, 255))
        pygame.draw.rect(self.screen, (200, 255, 0), self.make_button)
        self.screen.blit(make_text, (self.make_button.x + 40, self.make_button.y + 10))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if mouse clicked on input box
                    if self.input_box.collidepoint(event.pos):
                        self.is_input_active = True
                    else:
                        self.is_input_active = False
                    # Check if mouse clicked on return button
                    if self.return_button.collidepoint(event.pos):
                        running = False
                    # Check if mouse clicked on make button
                    if self.make_button.collidepoint(event.pos):
                        file_path = "/home/rpi/Desktop/AudioVisualization-main/DataFiles/" + self.input_text
                        with open(file_path, 'w') as file:
                            print(self.input_text)
                        print(self.input_text)
                elif event.type == pygame.KEYDOWN:
                    if self.is_input_active:
                        # Handle text input
                        if event.key == pygame.K_RETURN:
                            self.is_input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            self.input_text += event.unicode

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        #pygame.quit()
