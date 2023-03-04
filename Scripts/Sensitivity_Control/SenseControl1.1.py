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
PRINT_LOADED_SOUNDS_TO_CONSOLE = True      #
############################################


# [STEP 1] Load the binary file containing the sound recordings
raw_sounds = RawSound.read_from_file('../Regression_SandBox/data2.df')
SCISoundList = [] #prep the SCISound list
sensitivity_levels = []
for i, raw_sound in enumerate(raw_sounds):
    if(PRINT_LOADED_SOUNDS_TO_CONSOLE):
        print(raw_sound.times, raw_sound.a, raw_sound.b, raw_sound.c)
    # [STEP 2] Preprocess the data by extracting relevant features
    SCISoundInstance = SCISound(raw_sound)
    SCISoundList.append(SCISoundInstance)

# [STEP 3] Define the state space
state_size = SCISoundList[0].num_features + 1  # plus one for the current sensitivity level
# [STEP 4] Define the action space
action_size = 101  # 0 to 100 in increments of 1
# [STEP 5] Create the agent
agent = Agent(state_size, action_size)
# [STEP 6] Train the agent
for ss in SCISoundList:
    current_state = State(ss, sensitivity_levels)
    next_state, sensor_output = current_state.GetNextState(agent.get_action(current_state))

    # Calculate the reward based on the current and previous sensor outputs and actions
    reward = calculate_reward(sensor_output, prev_sensor_output, action, prev_action)

    # Update the agent's Q-value estimates based on the reward and transition to the next state
    agent.update(current_state, action, next_state, reward)

    prev_sensor_output = sensor_output
    prev_action = action

    # [STEP 7] Save the trained model if the performance is satisfactory
    if i % 1000 == 0:
        # Evaluate the performance of the model using the testing set
        test_accuracy = evaluate_performance(test_set, agent)
        if test_accuracy >= 0.9:
            agent.save_model('model.pkl')
