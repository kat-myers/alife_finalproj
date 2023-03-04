import numpy as np
import numpy.random as rand
import random

num_segments_1 = 3
num_segments_2 = 1
num_segments_3 = 1

cubes_b1 = []
total_cubes = []
joint_names = []

## instead, I will make each array and then append the cube_sizes_b1 guy
for i in range(num_segments_1):
    # np.array([1, 2, 3, 4])
    cubes_b1.append("i"+str(i))
    total_cubes.append("i"+str(i))
    if i == 0:
        joint_names.append('Torso_i'+str(0))
    if i < num_segments_1 - 1:
        joint_names.append("i"+str(i)+'_'+ "i"+str(i+1))
        joint_names.append("j"+str(i)+'_'+ "j"+str(i+1))
        joint_names.append("k"+str(i)+'_'+ "k"+str(i+1))

removal_index = []
for i in range(len(joint_names)):
    if cubes_b1[-1] in joint_names[i]:
        removal_index.append(i)

print(removal_index)
print(joint_names)
for val in reversed(removal_index):
    joint_names.remove(joint_names[val])
print(joint_names)





