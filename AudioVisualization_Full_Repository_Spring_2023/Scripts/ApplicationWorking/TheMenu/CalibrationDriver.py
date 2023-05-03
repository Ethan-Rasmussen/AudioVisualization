
import pygame
from InputBox import InputBox
from TextBox import TextBox
import sys
import os
#need to put the rawsoundbuffer.py path in here, at least for now, there wasnt time to sort this out
current_directory = os.path.dirname(os.path.abspath(__file__))
sandbox_directory = os.path.join(current_directory, '../..', 'Regression_SandBox')
sandbox_directory = os.path.normpath(sandbox_directory)  # Normalize the path (optional)
sys.path.append(sandbox_directory)
print(sys.path)
from RawSoundBuffer import RawSoundBuffer
from TestListener import listen_and_append
from RawSound import RawSound




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
        
    def Show_text(self,size, block_width, message):
        base1 = 195
        base2 = 85
        base3 = block_width
        box_height = size
        pointless_fontsize = 20
        n = 0
        block_boxes = set()

        # Split the message by newline character
        lines = message.split("\n")
        
        # Create a TextBox object for each line of the message
        for line in lines:
            box = TextBox(base1, base2+(n*box_height), base3, box_height, pointless_fontsize)
            box.yes_clear_b = False
            box.text = line.strip()  # Set the text of the TextBox to the line, removing leading/trailing whitespace
            block_boxes.add(box)
            n += 1
            
        return block_boxes


    
    def run(self):
        #------------------------------USER XYZ MODE INPUT BOX STUFF------------#|
        # Define input box dimensions and locations                             #|
        xval_input_box_rect = pygame.Rect(437, 45, 117, 47)                     #|
        yval_input_box_rect = pygame.Rect(436, 147, 117, 47)                    #|
        zval_input_box_rect = pygame.Rect(435, 253, 117, 47)                    #|
        #-------Locked_view----------------------------------                   #|
        xval_input_box_LOCKED_button_rect = pygame.Rect(291, 18, 58, 23)               #|
        yval_input_box_LOCKED_button_rect = pygame.Rect(290, 69, 59, 23)          #|
        zval_input_box_LOCKED_button_rect = pygame.Rect(290, 122, 58, 23)         #|
        # Define input box text                                                 #|
        xval_text = ""                                                          #|
        yval_text = ""                                                          #|
        zval_text = ""                                                          #|
        xval_text_LOCKED = ""                                                          #|
        yval_text_LOCKED = ""                                                          #|
        zval_text_LOCKED = ""    
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
        # Create input box instances                                            #|
        xval_input_box_LOCKED = InputBox(xval_input_box_LOCKED_button_rect, xval_text_LOCKED)               #|
        # Create a new text box
        xtext_box_LOCKED = TextBox(xval_input_box_LOCKED_button_rect.x, xval_input_box_LOCKED_button_rect.y, 58, 23, 21)
        xtext_box_LOCKED.yes_clear_b = False
        yval_input_box_LOCKED = InputBox(yval_input_box_LOCKED_button_rect, yval_text_LOCKED)               #|
        # Create a new text box
        ytext_box_LOCKED = TextBox(yval_input_box_LOCKED_button_rect.x, yval_input_box_LOCKED_button_rect.y, 59, 23, 21)
        ytext_box_LOCKED.yes_clear_b = False
        zval_input_box_LOCKED = InputBox(zval_input_box_LOCKED_button_rect, zval_text_LOCKED)               #|
        # Create a new text box
        ztext_box_LOCKED = TextBox(zval_input_box_LOCKED_button_rect.x, zval_input_box_LOCKED_button_rect.y, 58, 23, 21)
        ztext_box_LOCKED.yes_clear_b = False
        # Add input boxes to list
        
        # Define the text for the unavailable message
        unavailable_text = ("This mode is currently unavailable...\nuntil a future researcher" +
                            "implements it!\n<- Please use the other mode by clicking 'switch modes'")

        # Create a list of TextBox objects from the split text
        unavailable_messages = []
        base1 = 195
        base2 = 75
        base3 = 530
        box_height = 35
        pointless_fontsize = 20
        n = 0
        for line in unavailable_text.split('\n'):
            message_box = TextBox(base1, base2+(n*box_height), base3, box_height, pointless_fontsize)
            message_box.yes_clear_b = False
            message_box.text = line
            unavailable_messages.append(message_box)
            n += 1
        # Define the text for the unavailable message
        save_text = ("   Click this X------------->\n" +
                     "     after you finish\n"
                     "     calibrating to save\n" +
                     "     to 'cal_data.df'")

        # Create a list of TextBox objects from the split text
        save_messages = []
        base1 = 642
        base2 = 0
        base3 = 130
        box_height = 22
        pointless_fontsize = 20
        n = 0
        for line in save_text.split('\n'):
            message_box = TextBox(base1, base2+(n*box_height), base3, box_height, pointless_fontsize)
            message_box.yes_clear_b = False
            message_box.text = line
            save_messages.append(message_box)
            n += 1
        
         # Create a list of TextBox objects from the split text
         # Define the text for the unavailable message
        box_info = ("double click text_boxes to type in them.")
        box_info_messages = []
        base1 = 175
        base2 = 5
        base3 = 220
        box_height = 20
        pointless_fontsize = 20
        n = 0
        for line in box_info.split('\n'):
            message_box = TextBox(base1, base2+(n*box_height), base3, box_height, pointless_fontsize)
            message_box.yes_clear_b = False
            message_box.text = line
            box_info_messages.append(message_box)
            n += 1
            
#         # Create a set of all the message boxes
        block_boxes = set(unavailable_messages)
        block_boxes2 = set(save_messages)
        block_boxes3 = set(box_info_messages)
        input_boxes_LOCKED = [xval_input_box_LOCKED, yval_input_box_LOCKED, zval_input_box_LOCKED]          #|
        text_boxes_LOCKED = [xtext_box_LOCKED, ytext_box_LOCKED, ztext_box_LOCKED]          #|
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
        raw_sounds = []
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
                elif (locked_in ==True):
                    #move each text box to its new location and decrease the fontsize slightly
                    #new locations
                    for textbox in text_boxes_LOCKED:
                        textbox.draw(self.screen)
                
        #------------------------------------------------DEFAULT MODE----------------------------------------------------------#|
            if(mode == 'randomXYZ'):                                                                                           #|
                for box in block_boxes:
                    box.draw(self.screen, (230, 0, 0))                
#                 unavailable_message1_box.draw(self.screen)                                                                         #| #|
#                 unavailable_message2_box.draw(self.screen)                                                                         #| #|
                # Check for events                                                                                             #|
                for event in pygame.event.get():                                                                               #|
                                                                                                                               #|
                    # Quit the program when the user closes the window                                                         #|
                    if event.type == pygame.QUIT:                                                                              #|
                        running = False                                                                                        #|
                                                                                                                               #|
#                     # Check for button click                                                                                   #|
#                     if event.type == pygame.MOUSEBUTTONDOWN and big_left_button_rect.collidepoint(pygame.mouse.get_pos()):     #|
#                         # Do something when the begin_listening button is clicked                                              #|
#                         print("Parameters:", param1, param2, param3)                                                           #|
#                                                                                                                                #|
#                     if event.type == pygame.MOUSEBUTTONDOWN and top_left_button_rect.collidepoint(pygame.mouse.get_pos()):     #|
#                         #generate a new float value between 1.0 and 10.0 and print it to the                                        #|
#                         param1 = param1 + "NEW"
#                         param2 = param2 + "NEW"
#                         param3 = param3 + "NEW"
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
                if(locked_in == True):
                    # Draw input boxes
                    for box in text_boxes_LOCKED:
                        box.draw(self.screen)                                                                    #| #|
                    for box in block_boxes2:
                        box.draw(self.screen)
                    for i, text_box in enumerate(text_boxes_LOCKED):
#                             if pygame.mouse.get_pressed()[0] and text_box.rect.collidepoint(pygame.mouse.get_pos()):
#                                 text_box.run(self.screen, self.background)
                        None
                    for event in pygame.event.get():                                                                               #| #|
                                                                                                                                   #| #|
                        # Quit the program when the user closes the window                                                         #| #|
                        if event.type == pygame.QUIT:                                                                              #| #|
                            running = False                                                                                        #| #|
                                                                                                                                   #| #|
                                                                            #| #|
                                    
                        # Check for button click                                                                                   #| #|
                        actively_listening = False                                                                                                           #| #|
                        if event.type == pygame.MOUSEBUTTONDOWN and big_left_button_rect.collidepoint(pygame.mouse.get_pos()):    #| #|
                            # BIEGIN_LISTENING BUTTON CLICKED                                    #| #|
                            actively_listening = True
                            print("actively listening...")
                            if(actively_listening):
                                next_sound = listen_and_append()
                                next_sound.a = float(text_boxes_LOCKED[0].text)
                                next_sound.b = float(text_boxes_LOCKED[1].text)
                                next_sound.c = float(text_boxes_LOCKED[2].text)
                                raw_sounds.append(next_sound)                                                                      #| #|
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
                            running = False
                            
        #--------------------------------------------------------------------------------------------------------------------------#| #|
        #-----------------------------------------------unlocked STATE------------------------------------------------------------#| #|
                elif (locked_in == False):
                    # Draw input boxes
                    for box in input_boxes:
                        box.draw(self.screen)
                    for box in block_boxes2:
                        box.draw(self.screen)#| #|
                    for box in block_boxes3:
                        box.draw(self.screen, (0, 0, 255))#| #|
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
                                for i, tb in enumerate(text_boxes):
                                    text_boxes_LOCKED[i].text = tb.text
                                    if(text_boxes_LOCKED[i].text == "" or text_boxes_LOCKED[i].text == None or text_boxes_LOCKED[i].text == "."):
                                        text_boxes_LOCKED[i].text = "0.0"
                                    if(text_boxes_LOCKED[i].text[0] == '.'):
                                        temp = "0" + text_boxes_LOCKED[i].text
                                        text_boxes_LOCKED[i].text = temp
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
            # MAKE DATA FILE, TRAIN MODEL WITH FILE
            if event.type == pygame.MOUSEBUTTONDOWN and X_out_button_rect.collidepoint(pygame.mouse.get_pos()):        #| #|
                if (len(raw_sounds) > 0):
                    destination_file = "cal_data.df"
                    print(f" Generating {len(raw_sounds)} sounds in {destination_file}...")
                   # Write the list of RawSound objects to a file
                    with open(destination_file, 'wb') as f:
                        for raw_sound in raw_sounds:
                            f.write(raw_sound.to_bytes())
                    from Train_With_New_Sound_File import execute_training
                    
            # Update the display
            pygame.display.update()
            clock.tick(30)
        #pygame.quit()
