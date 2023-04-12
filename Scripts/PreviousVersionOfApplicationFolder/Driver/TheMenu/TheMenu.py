import pygame


class SoundVisualizationMenu:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.background = None
        self.font = pygame.font.SysFont(None, 30)
        self.clock = pygame.time.Clock()
        self.options = [
            "Start a new log file",
            "Single sound viewer",
            "Calibrate",
            "View a log file",
            "Help"
        ]
        self.selected_option = 0

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        x = 100
        y = 100
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))
            if i == self.selected_option:
                pygame.draw.rect(self.screen, (255, 0, 0), (x - 10, y - 5, text.get_width() + 20, text.get_height() + 10), 0)
            self.screen.blit(text, (x, y))
            y += text.get_height() + 10

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = max(0, self.selected_option - 1)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = min(len(self.options) - 1, self.selected_option + 1)
                    elif event.key == pygame.K_RETURN:
                        option = self.options[self.selected_option]
                        if option == "Start a new log file":
                            # handle this option
                            pass
                        elif option == "Single sound viewer":
                            # handle this option
                            pass
                        elif option == "Calibrate":
                            # handle this option
                            from Calibration import GeneratedCalibration
                            pass
                        elif option == "View a log file":
                            # handle this option
                            pass
                        elif option == "Help":
                            # handle this option
                            pass

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

def run_sound_visualization_menu():
    menu = SoundVisualizationMenu(800, 450)
    menu.background = pygame.image.load("main_menu_bg.png")
    menu.run()

