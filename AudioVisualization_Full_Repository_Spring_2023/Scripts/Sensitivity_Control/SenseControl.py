#   GOALS OF THIS PROGRAM:
#    1. Load the dataset containing sound recordings,
#        along with the corresponding timestamps and sensitivity levels.
#    2. Preprocess the data by extracting relevant features,
#        such as the time difference between the arrival of the sound signal at each microphone.
#    3. Split the dataset into training and testing sets.
#    4. Choose an appropriate machine learning algorithm,
#        such as a decision tree, random forest, or support vector machine, to train the model.
#    5. Train the model using the training set, using techniques such as cross-validation
#        to optimize the model's hyperparameters.
#    6. Evaluate the performance of the model using the testing set,
#        using metrics such as accuracy, precision, recall, and F1 score.
#    7. If the performance of the model is satisfactory, save the model for later use.
#        If not, return to step 4 and try a different algorithm or adjust the  
#        hyperparameters.
########################################################################################################
# Import the RawSound class from your code #
from random import random                 #
from RawSound import RawSound             #
from SoundFeatures import SoundFeatures   #
from SCISound import SCISound             #
from Agent import Agent                   #
from State import State                   #
from TDC import TDC                   #
PRINT_LOADED_SOUNDS_TO_CONSOLE = True      #
############################################



# [STEP 1] Load the binary file containing the sound recordings
raw_sounds = RawSound.read_from_file('../Regression_SandBox/data2.df')
SCISoundList = [] #prep the SCISound list
sensitivity_levels = []
# [STEP 4]   define the action space 
action_space = range(0, 101)
for i, raw_sound in enumerate(raw_sounds):
    if(PRINT_LOADED_SOUNDS_TO_CONSOLE):
        print(raw_sound.times, raw_sound.a, raw_sound.b, raw_sound.c)
    #_________________________________________
    # [STEP 2] sophisticate the sound data to be fed to the learning algorithm
    SCISoundInstance = SCISound(raw_sound)
    SCISoundList.append(SCISoundInstance)

#_________________________________________________________________________________|
# [STEP 3]   define the state space

    #'import State' does this by defining a class for type 'State'
    
#_________________________________________________________________________________|
# [STEP 4]   define the action space        



#_________________________________________________________________________________|
# [STEP 5]   define the reward
def calculate_reward(sensor_output, prev_sensor_output, action, prev_action):
    # Check if there was a trigger event
    if sensor_output == 1:
        reward = 1.0
    # Check if there was a false trigger event
    elif sensor_output == 1 and prev_sensor_output == 0:
        reward = -1.0
    else:
        reward = 0.0

    # Penalize the agent for changing sensitivity levels too frequently
    if action != prev_action:
        reward -= 0.1

    return reward


#_________________________________________________________________________________|
# [STEP 6]   define the transition function
def get_next_state(current_state, action):
    # Update the sensitivity levels based on the chosen action
    sensitivity_levels = action / 100.0
    
    # Simulate the sensor output using some function of the current state and the sensitivity levels
    sensor_output = current_state.SimulateSensorOutput(current_state, sensitivity_levels)
    
    # Create the next state object
    next_state = State(current_state.scisound, sensitivity_levels)
    
    return next_state, sensor_output 


#_________________________________________________________________________________|

# [STEP 7]   set up sensor output simulation
prev_sensor_output = 0
prev_action = 0
time_diff_classifier = TDC(SCISoundList)

for i in range(len(SCISoundList)):
    current_state = State(SCISoundList[i], sensitivity_levels)
    action = agent.get_action(current_state)
    next_state, sensor_output = get_next_state(current_state, action)

    # Use the SVM to simulate the sensor output based on the current state and sensitivity levels
    time_diffs = current_state.time_diffs
    sensor_output = time_diff_classifier.predict(time_diffs)

    # Calculate the reward based on the current and previous sensor outputs and actions
    reward = calculate_reward(sensor_output, prev_sensor_output, action, prev_action)

    # Update the agent's Q-value estimates based on the reward and transition to the next state
    agent.update(current_state, action, next_state, reward)

    prev_sensor_output = sensor_output
    prev_action = action
