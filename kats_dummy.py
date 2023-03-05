import numpy as np
import numpy.random as rand
import random

num_segments_1 = 3
num_segments_2 = 1
num_segments_3 = 1

cubes_b1 = []
total_cubes = []
joint_names = []
cube_sizes_b1 = []

for i in range(num_segments_1):
    cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
    cube_sizes_b1.append(cube_size_rand)
print(cube_sizes_b1)

body_coin = 1
if body_coin == 1:
    rand_n = random.randint(0,2)
    print(rand_n)
    for i in range(2):
        cube_sizes_b1[rand_n][i] = cube_sizes_b1[rand_n][i] *.5
print(cube_sizes_b1)



