
import pygame
from InputBox import InputBox
import sys

sys.path.append('/Users/bmors/Documents/CSC 465/project_scripts/Application/ourFont')
from ourFont import ourFont
# Initialize pygame
pygame.init()

# Set the size of the window and load the background image
screen = pygame.display.set_mode((800, 450))
background = pygame.image.load('Calibration_BG.png').convert()

# Set the font and font size
font = pygame.font.SysFont("Arial", 20)

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
yval_input_box = InputBox(yval_input_box_rect, yval_text)               #|
zval_input_box = InputBox(zval_input_box_rect, zval_text)               #|
# Add input boxes to list                                               #|
input_boxes = [xval_input_box, yval_input_box, zval_input_box]          #|
# Set active input box                                                  #|
active_input_box = None                                                 #|
#------------------------------USER XYZ MODE INPUT BOX STUFF------------#|

#-------UNIVERSAL BUTTONS--------------------------------#|
top_left_button_rect = pygame.Rect(19, 65, 117, 41)      #|
X_out_button_rect = pygame.Rect(770, 10, 30, 28)         #|
big_left_button_rect = pygame.Rect(19, 132, 117, 66)     #|
switch_modes_button_rect = pygame.Rect(20, 108, 116, 21) #|
#--------------------------------------------------------#|

# STATE CONTROL VARIABLES
mode = 'randomXYZ'
locked_in = False


running = True
# Set the main loop for the program
while running:
    # Draw the background image
    screen.blit(background, (0, 0))
#    if(mode == 'userXYZ'):
#        if (locked_in == False):
#            # Draw input boxes
#            for box in input_boxes:
#                box.draw(screen)
        
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
                # Do something when the gen_new_xyz_targets button is clicked                                          #|
                param1 = param1 + "NEW"                                                                                #|
                param2 = param2 + "NEW"                                                                                #|
                param3 = param3 + "NEW"                                                                                #|
                                                                                                                       #|
            if event.type == pygame.MOUSEBUTTONDOWN and switch_modes_button_rect.collidepoint(pygame.mouse.get_pos()): #|
                # Do something when the switch_modes button is clicked                                                 #|
                if(mode == 'randomXYZ'):                                                                               #|
                    mode = 'userXYZ'                                                                                   #|
                    background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #|
                else:                                                                                                  #|
                    mode = 'randomXYZ'                                                                                 #|
                    background = pygame.image.load('Calibration_BG.png').convert()                                     #|
                print(f"mode is now {mode}")                                                                           #|
                                                                                                                       #|
            if event.type == pygame.MOUSEBUTTONDOWN and X_out_button_rect.collidepoint(pygame.mouse.get_pos()):        #|
                # Do something when the X-out button is clicked                                                        #|
                running = False                                                                                        #|
#----------------------------------------------------------------------------------------------------------------------#|
                
                
#------------------------------------------------------------------------------USER XYZ MODE----------------------------------#|
#----------------------------------------------UNLOCKED STATE--------------------------------------------------------------#| #|
    elif(mode == 'userXYZ'):                                                                                               #| #|
        # Check for events                                                                                                 #| #|
        if(locked_in == True):                                                                                             #| #|
            for event in pygame.event.get():                                                                               #| #|
                                                                                                                           #| #|
                # Quit the program when the user closes the window                                                         #| #|
                if event.type == pygame.QUIT:                                                                              #| #|
                    running = False                                                                                        #| #|
                                                                                                                           #| #|
                for box in input_boxes:                                                                                    #| #|
                    box.handle_event(event, screen)                                                                        #| #|
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
                        background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #| #|
                        locked_in = False # enter locked in state                                                          #| #|
                    else:                                                                                                  #| #|
                        background = pygame.image.load('Calibration_BG_usermode_LOCKED.png').convert()                     #| #|
                        locked_in = True # enter locked in state                                                           #| #|
                                                                                                                           #| #|
                if event.type == pygame.MOUSEBUTTONDOWN and switch_modes_button_rect.collidepoint(pygame.mouse.get_pos()): #| #|
                    # Do something when the switch_modes button is clicked                                                 #| #|
                    if(mode == 'randomXYZ'):                                                                               #| #|
                        mode = 'userXYZ'                                                                                   #| #|
                        background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #| #|
                    else:                                                                                                  #| #|
                        mode = 'randomXYZ'                                                                                 #| #|
                        background = pygame.image.load('Calibration_BG.png').convert()                                     #| #|
                    print(f"mode is now {mode}")                                                                           #| #|
                                                                                                                           #| #|
                if event.type == pygame.MOUSEBUTTONDOWN and X_out_button_rect.collidepoint(pygame.mouse.get_pos()):        #| #|
                    # Do something when the X-out button is clicked                                                        #| #|
                    running = False                                                                                        #| #|
#--------------------------------------------------------------------------------------------------------------------------#| #|
#-----------------------------------------------LOCKED-IN STATE------------------------------------------------------------#| #|
        elif (locked_in == False):
            # Draw input boxes
            for box in input_boxes:
                box.draw(screen)                                                                            #| #|
            for event in pygame.event.get():                                                                              #| #|
                                                                                                                           #| #|
                # Quit the program when the user closes the window                                                         #| #|
                if event.type == pygame.QUIT:                                                                              #| #|
                    running = False                                                                                        #| #|
                if event.type == pygame.MOUSEBUTTONDOWN:                                                                   #| #|
                    for box in input_boxes:                                                                                #| #|
                        if box.rect.collidepoint(event.pos):                                                               #| #|
                            active_input_box = box                                                                         #| #|
                            print(f"{box} is currently selected")                                                          #| #|
                        else:                                                                                              #| #|
                            box.active = False                                                                             #| #|
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
                        background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #| #|
                        locked_in = False # enter locked in state                                                          #| #|
                    else:                                                                                                  #| #|
                        background = pygame.image.load('Calibration_BG_usermode_LOCKED.png').convert()                     #| #|
                        locked_in = True # enter locked in state                                                           #| #|
                                                                                                                           #| #|
                                                                                                                           #| #|
                if event.type == pygame.MOUSEBUTTONDOWN and switch_modes_button_rect.collidepoint(pygame.mouse.get_pos()): #| #|
                    # Do something when the switch_modes button is clicked                                                 #| #|
                    if(mode == 'randomXYZ'):                                                                               #| #|
                        background = pygame.image.load('Calibration_BG_usermode_UNLOCKED.png').convert()                   #| #|
                        mode = 'userXYZ'                                                                                   #| #|
                    else:                                                                                                  #| #|
                        mode = 'randomXYZ'                                                                                 #| #|
                        background = pygame.image.load('Calibration_BG.png').convert()                                     #| #|
                    print(f"mode is now {mode}")                                                                           #| #|
                                                                                                                           #| #|
                if event.type == pygame.MOUSEBUTTONDOWN and X_out_button_rect.collidepoint(pygame.mouse.get_pos()):        #| #|
                    # Do something when the X-out button is clicked                                                        #| #|
                    running = False                                                                                        #| #|
#--------------------------------------------------------------------------------------------------------------------------#| #|
#-----------------------------------------------------------------------------------------------------------------------------#|
                    

    # Update the display
    pygame.display.update()
pygame.quit()
