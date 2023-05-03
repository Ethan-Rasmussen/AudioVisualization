'''
The Agent class initializes a Q-table with dimensions (state_size, action_size)
and provides methods for getting an action based on the current state, updating
the Q-value estimates based on the reward and transition to the next state, and
adjusting the exploration rate during training.

The get_action method chooses a random action with probability exploration_rate or
chooses the action with the highest Q-value for the current state.

The update method updates the Q-value estimate for the current state-action pair based
on the reward and the maximum Q-value for the next state. The Q-value is updated using
the TD-error formula, which measures the difference between the observed reward and the
expected reward based on the current Q-value estimate. The Q-value is then updated using
the learning rate and the TD-error.

You can instantiate an Agent object with the appropriate state size and action size, and
then use the get_action and update methods in the main training loop to train the agent.
'''

import numpy as np

class Agent:
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.5):
        self.current_state = 0
        self.current_size = 0
        self.state_size = state_size
        self.action_size = action_size
        self.q_table = np.zeros((state_size, action_size))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
    
    def get_action(self, state=0):
        if np.random.rand() < self.exploration_rate:
            # Choose a random action with probability epsilon
            action = np.random.choice(self.action_size)
        else:
            # Choose the action with the highest Q-value for the current state
            q_values = self.q_table[self.current_state, :]
            max_q_value = np.max(q_values)
            action = np.random.choice(np.where(q_values == max_q_value)[0])
        
        return action
    
    def update(self, current_state, action, next_state, reward):
        # Update the Q-value estimate for the current state-action pair
        q_value = self.q_table[current_state.time_diffs, current_state.current_levels, action]
        max_q_value = np.max(self.q_table[next_state.time_diffs, next_state.current_levels, :])
        td_error = reward + self.discount_factor * max_q_value - q_value
        self.q_table[current_state.time_diffs, current_state.current_levels, action] += self.learning_rate * td_error

