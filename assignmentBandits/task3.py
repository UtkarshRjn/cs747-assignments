"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the AlgorithmManyArms class. Here are the method details:
    - __init__(self, num_arms, horizon): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, reward): This method is called just after the 
        give_pull method. The method should update the algorithm's internal
        state based on the arm that was pulled and the reward that was received.
        (The value of arm_index is the same as the one returned by give_pull.)
"""

import numpy as np

# START EDITING HERE
# You can use this space to define any helper functions that you need
# END EDITING HERE

class AlgorithmManyArms:
    def __init__(self, num_arms, horizon):
        self.num_arms = num_arms
        # Horizon is same as number of arms
        # START EDITING HERE
        self.horizon = horizon
        self.actual_num_arms = num_arms // 100
        self.index_map = np.random.choice(num_arms, self.actual_num_arms , replace=False)
        self.success = np.zeros(self.actual_num_arms)
        self.failure = np.zeros(self.actual_num_arms)
        # You can add any other variables you need here
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        return self.index_map[np.argmax(np.random.beta(self.success + 1, self.failure + 1))]
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        i, = np.where(self.index_map == arm_index) # integers
        if reward == 1:
            self.success[i] += 1
        else:
            self.failure[i] += 1
        # END EDITING HERE
