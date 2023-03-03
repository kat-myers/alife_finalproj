import numpy as np
import numpy.random as rand
import random

num_segments_1 = 2
num_segments_2 = 1
num_segments_3 = 1

cube_sizes_b1 = np.zeros(num_segments_1)
cube_sizes_b2 = np.zeros(num_segments_2)
cube_sizes_b3 = np.zeros(num_segments_3)


## instead, I will make each array and then append the cube_sizes_b1 guy
for i in range(len(cube_sizes_b1)):
    # np.array([1, 2, 3, 4])
    cube_size_rand =  np.array([random.uniform(.3,1),random.uniform(.3,1),random.uniform(.3,1)]) 
    cube_sizes_b1.append