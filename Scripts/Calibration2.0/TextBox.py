import pygame
class TextBox:
    def __init__(self, x, y, width, height, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = "5.0"
        self.active = False
        self.font = pygame.font.Font("RobotoCondensed-Regular.ttf", 20)
        self.cursor_visible = False
        self.cursor_timer = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked inside the rect
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

            # Check if the user clicked the clear button
            clear_button_rect = pygame.Rect(self.rect.right + 5, self.rect.top, 20, 20)
            if pygame.mouse.get_pressed()[0] and clear_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.text = ""

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                print(self.text)
                self.text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isnumeric() or event.unicode == ".":
                # Only allow numbers and a single decimal point
                if event.unicode == "." and "." in self.text:
                    pass
                else:
                    self.text += event.unicode

    def draw(self, screen):
        # Change the background color if the text box is active
        if self.active:
            pygame.draw.rect(screen, (200, 200, 200), self.rect)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        # Render the text
        text_surface = self.font.render(self.text, True, (0, 0, 0))

        # Blit the text surface onto the screen
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 9))

        # Draw the cursor if the text box is active and the cursor timer is less than 15
        if self.active and self.cursor_visible:
            cursor_rect = pygame.Rect(self.rect.x + 5 + text_surface.get_width(), self.rect.y+9, 3, text_surface.get_height()-5)
            pygame.draw.rect(screen, (0, 0, 0), cursor_rect)

        # Increment the cursor timer
        self.cursor_timer += 1
        if self.cursor_timer >= 400:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0
        # Draw the clear button
        clear_button_rect = pygame.Rect(self.rect.right + 5, self.rect.top, 20, 20)
        pygame.draw.rect(screen, (255, 0, 0), clear_button_rect)

    def run(self, screen, bg):
        while True:
            screen.blit(bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    self.handle_event(event)

#            # Draw the screen
#            screen.fill((0, 0, 0))
            self.draw(screen)
            pygame.display.flip()

            # Break out of the loop if the user clicks outside of the text box
            if pygame.mouse.get_pressed()[0] and not self.rect.collidepoint(pygame.mouse.get_pos()):
                break


    def clear_text(self):
        self.text = ""
