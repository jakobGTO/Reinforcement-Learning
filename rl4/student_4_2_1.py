#!/usr/bin/env python3
# rewards: [golden_fish, jellyfish_1, jellyfish_2, ... , step]
rewards = [10, -10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10]

# Q learning learning rate
#No learning
alpha = 0.00001

# Q learning discount rate
#High exploration
gamma = 0.999999

# Epsilon initial
epsilon_initial = 1

# Epsilon final, this = 1 leads to no annealing
epsilon_final = 1

# Annealing timesteps
annealing_timesteps = 1000

# threshold
threshold = 1e-6
