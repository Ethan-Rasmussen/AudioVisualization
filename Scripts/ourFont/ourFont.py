import os
import pygame
import sys


class ourFont:
    def __init__(self, font_folder='/Users/bmors/Documents/CSC 465/project_scripts/Application/ourFont'):
        #self.font_folder = font_folder
       


        fontFolder = os.getcwd()
#-------------------------------------------------------------------------------#|
#PROPER FORMAT FOR IMPORTING A FILE(from within 'Application' folder somewhere) #|
############################################################################### #|
        currentDirectory = ''                                                   #|
        sys.path.append(fontFolder)                                             #|
        currentDirectory = fontFolder + '/ourFont'                              #|
        from ourFont import ourFont                                             #|
        sys.path.append(currentDirectory)                                       #|
#-------------------------------------------------------------------------------#|
        font_folder = currentDirectory

        self.char_width = 12
        self.char_height = 21
        self.char_dict = self.load_characters()
        self.text = 'snipeshow'

    def load_characters(self):
        char_dict = {}
        for file in os.listdir(self.font_folder):
            if file.endswith('.png'):
                char_key = self.get_char_key(file)
                char_image = pygame.image.load(os.path.join(self.font_folder, file))
                char_dict[char_key] = char_image
        return char_dict

    def get_char_key(self, filename):
        def get_char_key(self, filename):
            char_key_mapping = {
                '_!.png': '!', '_SLASH.png': '/', '_ASTERISK.png': '*', '_minus.png': '-', '_PLUS.png': '+', '_SPACE.png': ' ',
                'a.png': 'a', 'b.png': 'b', 'c.png': 'c', 'd.png': 'd', 'e.png': 'e', 'f.png': 'f', 'g.png': 'g', 'h.png': 'h',
                'i.png': 'i', 'j.png': 'j', 'k.png': 'k', 'l.png': 'l', 'm.png': 'm', 'n.png': 'n', 'o.png': 'o', 'p.png': 'p',
                'q.png': 'q', 'r.png': 'r', 's.png': 's', 't.png': 't', 'u.png': 'u', 'v.png': 'v', 'w.png': 'w', 'x.png': 'x',
                'y.png': 'y', 'z.png': 'z', 'BUpng': 'B', 'CU.png': 'C', 'DU.png': 'D', 'EUpng': 'E', 'FU.png': 'F', 'GU.png': 'G',
                'HU.png': 'H', 'IU.png': 'I', 'JU.png': 'J', 'KU.png': 'K', 'LU.png': 'L', 'MU.png': 'M', 'NU.png': 'N',
                'OU.png': 'O', 'PU.png': 'P', 'QU.png': 'Q', 'RU.png': 'R', 'SU.png': 'S', 'TU.png': 'T', 'UU.png': 'U',
                'VU.png': 'V', 'WU.png': 'W', 'XU.png': 'X', 'YU.png': 'Y', 'ZU.png': 'Z',
                '_0.png': '0', '_1.png': '1', '_2.png': '2', '_3.png': '3', '_4.png': '4', '_5.png': '5', '_6.png': '6',
                '_7.png': '7', '_8.png': '8', '_9.png': '9'
            }
            return char_key_mapping.get(filename)
    def get_filename_key(self, character):
        char_key_mapping = {
                '_!.png': '!', '_SLASH.png': '/', '_ASTERISK.png': '*', '_minus.png': '-', '_PLUS.png': '+', '_SPACE.png': ' ',
                'a.png': 'a', 'b.png': 'b', 'c.png': 'c', 'd.png': 'd', 'e.png': 'e', 'f.png': 'f', 'g.png': 'g', 'h.png': 'h',
                'i.png': 'i', 'j.png': 'j', 'k.png': 'k', 'l.png': 'l', 'm.png': 'm', 'n.png': 'n', 'o.png': 'o', 'p.png': 'p',
                'q.png': 'q', 'r.png': 'r', 's.png': 's', 't.png': 't', 'u.png': 'u', 'v.png': 'v', 'w.png': 'w', 'x.png': 'x',
                'y.png': 'y', 'z.png': 'z', 'BUpng': 'B', 'CU.png': 'C', 'DU.png': 'D', 'EUpng': 'E', 'FU.png': 'F', 'GU.png': 'G',
                'HU.png': 'H', 'IU.png': 'I', 'JU.png': 'J', 'KU.png': 'K', 'LU.png': 'L', 'MU.png': 'M', 'NU.png': 'N',
                'OU.png': 'O', 'PU.png': 'P', 'QU.png': 'Q', 'RU.png': 'R', 'SU.png': 'S', 'TU.png': 'T', 'UU.png': 'U',
                'VU.png': 'V', 'WU.png': 'W', 'XU.png': 'X', 'YU.png': 'Y', 'ZU.png': 'Z',
                '_0.png': '0', '_1.png': '1', '_2.png': '2', '_3.png': '3', '_4.png': '4', '_5.png': '5', '_6.png': '6',
                '_7.png': '7', '_8.png': '8', '_9.png': '9'
                }
        reverse_mapping = {value: key for key, value in char_key_mapping.items()}
        return reverse_mapping.get(character)


    def render_text(self, text, screen, x, y):
        CHUNK_TOP = y
        LEFT_MARGIN = x
        for char in text:
            if(x >= 800):
                x = LEFT_MARGIN
                y += 21
            if not(char == ''):
                try:
                    char_image_name = self.get_filename_key(f"{self.font_folder}/{char}")
                finally:                    
                    if(char.isalpha() and char.isupper()):
                        char_image_name = f"{self.font_folder}/{char}U.png"
                    elif(char.isalpha()):
                        char_image_name = f"{self.font_folder}/{char}.png"
                    elif(char == '/'):
                        char_image_name = f"{self.font_folder}/_SLASH.png"
                    elif(char == '*'):
                        char_image_name = f"{self.font_folder}/_ASTERISK.png"
                    elif(char == '-'):
                        char_image_name = f"{self.font_folder}/_DASH.png"
                    elif(char == '+'):
                        char_image_name = f"{self.font_folder}/_PLUS.png"
                    elif(char == ' '):
                        char_image_name = f"{self.font_folder}/_SPACE.png"
                    else:
                        char_image_name = f"{self.font_folder}/_{char}.png"
                char_image = pygame.image.load(char_image_name)
                screen.blit(char_image, (x,y))                
                x += self.char_width
                return(char_image, (x,y))
                
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

## Pygame window setup
#pygame.init()
#screen_width, screen_height = 800, 600
#screen = pygame.display.set_mode((screen_width, screen_height))
#pygame.display.set_caption('Our Font Example')
#
## Our font setup
#font_folder = '/Users/bmors/Documents/CSC 465/project_scripts/Application/ourFont'
#font = ourFont(font_folder)
#
## Main loop
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#
#    screen.fill((255, 255, 255))
#    font.render_text('the quick brown fox jumps over the lazy dog.', screen, 100, 100)
#    font.render_text('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.', screen, 100, 124)
#    font.render_text('0123456789./*-+!,', screen, 100, 148)
#    font.render_text('SGFBSGNGERNfdgbgnuyktt463ik4,', screen, 100, 172)
#    pygame.display.flip()
#
#pygame.quit()
