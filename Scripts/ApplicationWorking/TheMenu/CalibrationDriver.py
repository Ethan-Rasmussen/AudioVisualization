
import pygame
from InputBox import InputBox
from TextBox import TextBox
import sys
import os

class Calibration:
    def __init__(self, screen, width, height):
        # Initialize pygame
        pygame.init()
        self.screen = screen
        # Set the size of the window and load the background image
        self.screen = pygame.display.set_mode((800, 450))
        print(os.getcwd())
        self.background = pygame.image.load('Calibration_BG.png').convert()
        
        # Set the font and font size
        font = pygame.font.SysFont("Arial", 20)        
    
    def run(self):
        #------------------------------USER XYZ MODE INPUT BOX STUFF------------#|
        # Define input box dimensions and locations                             #|
        xval_input_box_rect = pygame.Rect(437, 45, 117, 47)                     #|
        yval_input_box_rect = pygame.Rect(436, 147, 117, 47)                    #|
        zval_input_box_rect = pygame.Rect(435, 253, 117, 47)                    #|
        # Define input box text                                                 #|
        xval_text = ""                                                          #|
        yval_text = ""                                                          #|
        zval_text = ""                                                          #|
        # Define text input box colors                                          #|
        active_color = pygame.Color('lightskyblue3')                            #|
        inactive_color = pygame.Color('gray15')                                 #|
        # Define input box input_box_font                                       #|
        input_box_font = pygame.font.Font(None, 32)                            #|
        # Create input box instances                                            #|
        xval_input_box = InputBox(xval_input_box_rect, xval_text)               #|
        # Create a new text box
        xtext_box = TextBox(xval_input_box_rect.x, xval_input_box_rect.y, 117, 47, 42)
        yval_input_box = InputBox(yval_input_box_rect, yval_text)               #|
        # Create a new text box
        ytext_box = TextBox(yval_input_box_rect.x, yval_input_box_rect.y, 117, 47, 42)
        zval_input_box = InputBox(zval_input_box_rect, zval_text)               #|
        # Create a new text box
        ztext_box = TextBox(zval_input_box_rect.x, zval_input_box_rect.y, 117, 47, 42)
        # Add input boxes to list                                               #|
        input_boxes = [xval_input_box, yval_input_box, zval_input_box]          #|
        text_boxes = [xtext_box, ytext_box, ztext_box]          #|

        # Set active input box                                                  #|
        active_input_box = None                                                 #|
        #------------------------------USER XYZ MODE INPUT BOX STUFF------------#|

        #-------UNIVERSAL BUTTONS--------------------------------#|
        top_left_button_rect = pygame.Rect(19, 65, 117, 41)      #|
        X_out_button_rect = pygame.Rect(770, 10, 30, 28)         #|
        big_left_button_rect = pygame.Rect(19, 132, 117, 66)     #|
        switch_modes_button_rect = pygame.Rect(20, 108, 116, 21) #|
        #--------------------------------------------------------#|
        clock = pygame.time.Clock()
        mode = 'randomXYZ'
        locked_in = False
        running = True
        # Set the main loop for the program
        while running:
            # Draw the background image
            self.screen.blit(self.background, (0, 0))
            if(mode == 'userXYZ'):
                if (locked_in == False):
                    # Draw input boxes
                    for box in input_boxes:
                        box.draw(self.screen)
                    self.screen.blit(self.background, (0, 0))
                    for textbox in text_boxes:
                        textbox.draw(self.screen)
                
        #------------------------------------------------DEFAULT MODE----------------------------------------------------------#|
            if(mode == 'randomXYZ'):                                                                                           #|
                # Check for events                                                                                             #|
                for event in pygame.event.get():                                                                               #|
                                                                                                                               #|
                    # Quit the program when the user closes the window                                                         #|
                    if event.type == pygame.QUIT:                                                                              #|
                        running = False                                                                                        #|
                                                                                                                               #|
                    # Check for button click                                                                                   #|
                    if event.type == pygame.MOUSEBUTTONDOWN and big_left_button_rect.collidepoint(pygame.mouse.get_pos()):     #|
                        # Do something when the begin_listening button is clicked                                              #|
                        print("Parameters:", param1, param2, param3)                                                           #|
                                                                                                                               #|
                    if event.type == pygame.MOUSEBUTTONDOWN and top_left_button_rect.collidepoint(pygame.mouse.get_pos()):     #|
                        #generate a new float value between 1.0 and 10.0 and print it to the                                        #|
                        param1 = param1 + "NEW"
                        param2 = param2 + "NEW"
                        param3 = param3 + "NEW"
                                                                                                                               #|
                    if event.type == pygame.MOUSEBUTTONDOWN and switch_modes_button_rect.collidepoint(pygame.mouse.get_pos()): #|
                        # Do something when the switch_modes button is clicked                                                 #|
                        if(mode == 'randomXYZ'):                                                                               #|
                            mode = 'userXYZ'                                                                                   #|
                            self.background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #|
                        else:                                                                                                  #|
                            mode = 'randomXYZ'                                                                                 #|
                            self.background = pygame.image.load('Calibration_BG.png').convert()                                     #|
                        print(f"mode is now {mode}")                                                                           #|
                                                                                                                               #|
                    if event.type == pygame.MOUSEBUTTONDOWN and X_out_button_rect.collidepoint(pygame.mouse.get_pos()):        #|
                        # Do something when the X-out button is clicked                                                        #|
                        running = False                                                                                        #|
        #----------------------------------------------------------------------------------------------------------------------#|
                        
                        
        #------------------------------------------------------------------------------USER XYZ MODE----------------------------------#|
        #----------------------------------------------locked STATE--------------------------------------------------------------#| #|
            elif(mode == 'userXYZ'):                                                                                               #| #|
                # Check for events                                                                                                 #| #|
                if(locked_in == True):                                                                                             #| #|
                    for event in pygame.event.get():                                                                               #| #|
                                                                                                                                   #| #|
                        # Quit the program when the user closes the window                                                         #| #|
                        if event.type == pygame.QUIT:                                                                              #| #|
                            running = False                                                                                        #| #|
                                                                                                                                   #| #|
                                                                            #| #|
                                    
                        # Check for button click                                                                                   #| #|
                                                                                                                                   #| #|
                        #BUTTON DISABLED IN THIS STATE                                                                             #| #|
        #                if event.type == pygame.MOUSEBUTTONDOWN and big_left_button_rect.collidepoint(pygame.mouse.get_pos()):    #| #|
        #                    # Do something when the begin_listening button is clicked                                             #| #|
        #                    print("Parameters:", param1, param2, param3)                                                          #| #|
                                                                                                                                   #| #|
                        if event.type == pygame.MOUSEBUTTONDOWN and top_left_button_rect.collidepoint(pygame.mouse.get_pos()):     #| #|
                            # Do something when the gen_new_xyz_targets button is clicked                                          #| #|
                            if(locked_in):                                                                                         #| #|
                                self.background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #| #|
                                locked_in = False # enter locked in state                                                          #| #|
                            else:                                                                                                  #| #|
                                self.background = pygame.image.load('Calibration_BG_usermode_LOCKED.png').convert()                     #| #|
                                locked_in = True # enter locked in state                                                           #| #|
                                                                                                                                   #| #|
                        if event.type == pygame.MOUSEBUTTONDOWN and switch_modes_button_rect.collidepoint(pygame.mouse.get_pos()): #| #|
                            # Do something when the switch_modes button is clicked                                                 #| #|
                            if(mode == 'randomXYZ'):                                                                               #| #|
                                mode = 'userXYZ'                                                                                   #| #|
                                self.background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #| #|
                            else:                                                                                                  #| #|
                                mode = 'randomXYZ'                                                                                 #| #|
                                self.background = pygame.image.load('Calibration_BG.png').convert()                                     #| #|
                            print(f"mode is now {mode}")                                                                           #| #|
                                                                                                                                   #| #|
                        if event.type == pygame.MOUSEBUTTONDOWN and X_out_button_rect.collidepoint(pygame.mouse.get_pos()):        #| #|
                            # Do something when the X-out button is clicked                                                        #| #|
                            running = False                                                                                        #| #|
        #--------------------------------------------------------------------------------------------------------------------------#| #|
        #-----------------------------------------------unlocked STATE------------------------------------------------------------#| #|
                elif (locked_in == False):
                    # Draw input boxes
                    for box in input_boxes:
                        box.draw(self.screen)                                                                         #| #|
                    for i, text_box in enumerate(text_boxes):
                            if pygame.mouse.get_pressed()[0] and text_box.rect.collidepoint(pygame.mouse.get_pos()):
                                text_box.run(self.screen, self.background)                    
                    for event in pygame.event.get():                                                                              #| #|
                                                                                                                                   #| #|
                        # Quit the program when the user closes the window                                                         #| #|
                        if event.type == pygame.QUIT:                                                                              #| #|
                            running = False                                                                                        #| #|
                        if event.type == pygame.MOUSEBUTTONDOWN:                                                                   #| #|
        #                    for box in input_boxes:                                                                                #| #|
        #                        if box.rect.collidepoint(event.pos):                                                               #| #|
        #                            active_input_box = box                                                                         #| #|
        #                            print(f"{box} is currently selected")                                                          #| #|
        #                            #ourFont.run_keypad(typing_location=(100,300), screen=None)
        #                        else:                                                                                              #| #|
        #                            box.active = False                                                                             #| #|
                            None
                        else:                                                                                                      #| #|
                            active_input_box = None                                                                                #| #|
                        # Update input boxes with user input                                                                       #| #|
                        if event.type == pygame.KEYDOWN:                                                                           #| #|
                            if active_input_box:                                                                                   #| #|
                                active_input_box.handle_event(event)                                                               #| #|
                                                                                                                                   #| #|
                        if event.type == pygame.MOUSEBUTTONDOWN and top_left_button_rect.collidepoint(pygame.mouse.get_pos()):     #| #|
                            # Do something when the gen_new_xyz_targets button is clicked                                          #| #|
                            if(locked_in):                                                                                         #| #|
                                self.background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #| #|
                                locked_in = False # enter locked in state                                                          #| #|
                            else:                                                                                                  #| #|
                                self.background = pygame.image.load('Calibration_BG_usermode_LOCKED.png').convert()                     #| #|
                                locked_in = True # enter locked in state                                                           #| #|
                                                                                                                                   #| #|
                                                                                                                                   #| #|
                        if event.type == pygame.MOUSEBUTTONDOWN and switch_modes_button_rect.collidepoint(pygame.mouse.get_pos()): #| #|
                            # Do something when the switch_modes button is clicked                                                 #| #|
                            if(mode == 'randomXYZ'):                                                                               #| #|
                                self.background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #| #|
                                mode = 'userXYZ'                                                                                   #| #|
                            else:                                                                                                  #| #|
                                mode = 'randomXYZ'                                                                                 #| #|
                                self.background = pygame.image.load('Calibration_BG.png').convert()                                     #| #|
                            print(f"mode is now {mode}")                                                                           #| #|
                                                                                                                                   #| #|
                        if event.type == pygame.MOUSEBUTTONDOWN and X_out_button_rect.collidepoint(pygame.mouse.get_pos()):        #| #|
                            # Do something when the X-out button is clicked                                                        #| #|
                            running = False                                                                                        #| #|
                            
                    for textbox in text_boxes:
                        textbox.draw(self.screen)
                        textbox.handle_event(event)    
        #--------------------------------------------------------------------------------------------------------------------------#| #|
        #-----------------------------------------------------------------------------------------------------------------------------#|
                          

            # Update the display
            pygame.display.update()
            clock.tick(30)
        #pygame.quit()
