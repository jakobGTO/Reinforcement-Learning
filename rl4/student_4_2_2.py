#!/usr/bin/env python3
# rewards: [golden_fish, jellyfish_1, jellyfish_2, ... , step]
rewards = [-10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10]

# Q learning learning rate
# High learning
alpha = 0.9999

# Q learning discount rate
# High discovery
gamma = 0.9999

# Epsilon initial
epsilon_initial = 1

# Epsilon final
# Epsilon anneals down to 0
epsilon_final = 0

# Annealing timesteps
annealing_timesteps = 1000

# threshold
threshold = 1e-6
