import numpy as np
import numpy.random as rand
import random
import pyrosim.pyrosim as pyrosim
import os
import time
import constants as c


class SOLUTION:

    def __init__(self, nextAvailableID):
        """ init runs once every individual and their lineage, 
        so a population = 5 gen = 1, init runs 5 times
        population = 1 generation = 5, init runts 1 time"""
        
        
        self.weights = 0
        self.myID = nextAvailableID

        self.numMotors = 0
        self.numSensors = 0

        self.joint_names = []
        self.sensor_cubes = ['Torso']
        self.total_cubes = ['Torso']


        """ In the lines below, I generate the initial body plan for the parent in each lineage
        I generate the number of cubes / branch, each cube's size, and whether or not they are a sensor.
        
        I also generate the names of each cube and generate the joint_names so that these are able to be mutated in Mutate()"""
        
        
        ### Initializing Cube Existence, Size, and Names
        self.cubes_b1 = []
        self.cubes_b2 = []
        self.cubes_b3 = []

        self.max_seg_size = 4

        # self.num_segments_1 = random.randint(1,self.max_seg_size)
        # self.num_segments_2 = random.randint(1,self.max_seg_size)
        # self.num_segments_3 = random.randint(1,self.max_seg_size)

        self.num_segments_1 = 2
        self.num_segments_2 = 2
        self.num_segments_3 = 2

        self.cube_sizes_b1 = []
        self.cube_sizes_b2 = []
        self.cube_sizes_b3 = []
        
        for i in range(self.num_segments_1):
            self.cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
            self.cube_sizes_b1.append(self.cube_size_rand)
            self.cubes_b1.append("i"+str(i))
            self.total_cubes.append("i"+str(i))
            if i == 0:
                self.joint_names.append('Torso_i'+str(0))
            if i < self.num_segments_1 - 1:
                self.joint_names.append("i"+str(i)+'_'+ "i"+str(i+1))

        for i in range(self.num_segments_2):
            self.cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
            self.cube_sizes_b2.append(self.cube_size_rand)
            self.cubes_b2.append("j"+str(i))
            self.total_cubes.append("j"+str(i))
            if i == 0:
                self.joint_names.append("Torso_j"+str(0))
            if i < self.num_segments_2 - 1:
                self.joint_names.append("j"+str(i)+'_'+ "j"+str(i+1))
        
        for i in range(self.num_segments_3):
            self.cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
            self.cube_sizes_b3.append(self.cube_size_rand)
            self.cubes_b3.append("k"+str(i))
            self.total_cubes.append("k"+str(i))
            if i == 0:
                self.joint_names.append("Torso_k"+str(0))
            if i < self.num_segments_3 - 1:
                self.joint_names.append("k"+str(i)+'_'+ "k"+str(i+1))

        self.torso_size = np.zeros(3)
        for x in range(3):
            self.torso_size[x] = random.uniform(.3,1) * 1.3
        # self.cube_sizes = random.uniform(.2,1) *.9

        
        ### Initializing Cube Sensoring
        self.cube_sensors_b1 = []
        self.cube_sensors_b2 = []
        self.cube_sensors_b3 = []


        for i in range(self.num_segments_1):
            cube_sense = random.choice((True,False))
            self.cube_sensors_b1.append(cube_sense)
            if self.cube_sensors_b1[i] == True:
                self.sensor_cubes.append(self.cubes_b1[i])

        for i in range(self.num_segments_2):
            cube_sense = random.choice((True,False))
            self.cube_sensors_b2.append(cube_sense)
            if self.cube_sensors_b2[i] == True:
                self.sensor_cubes.append(self.cubes_b2[i])

        for i in range(self.num_segments_3):
            cube_sense = random.choice((True,False))
            self.cube_sensors_b3.append(cube_sense)
            if self.cube_sensors_b3[i] == True:
                self.sensor_cubes.append(self.cubes_b3[i])
    
        self.weights = np.random.rand(10,10) * 2 - 1
      

    def Set_ID(self, val): 
        self.myID = val



    def Start_Simulation(self, directOrGUI):

        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
    
        os.system("start /B py simulate.py " + str(directOrGUI) + " " + str(self.myID))
    


    def Wait_For_Simulation_To_End(self):

        fitnessFileName = 'fitness'+str(self.myID)+'.txt'
        while not os.path.exists(fitnessFileName):
            time.sleep(1)

        f = open(fitnessFileName, "r")
        self.fitness = float(f.readlines()[0])

        f.close()
        os.system("del " + "fitness" + str(self.myID) + ".txt")  



    def Create_World(self):

        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()



    def Create_Body(self):

        # define color codes
        green_code='    <color rgba="0 1.0 0.0 1.0"/>'
        green_name = '<material name="Green">'

        blue_code='    <color rgba="0 1.0 1.0 1.0"/>'
        blue_name = '<material name="Cyan">'

        red_code='    <color rgba="1.0 0 0 1.0"/>'
        red_name = '<material name="Red">'


        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        # [ movement away from camera (farther away from the origin of the thing), movement left and right, up and down]
        
        ### MAKE THE TORSO
        pyrosim.Send_Cube(color_code = green_code, color_name = green_name, name = "Torso", pos= [0,0,self.torso_size[2]*1.5], size= self.torso_size)
        

        ### BRANCH 1
        n = 0
        if self.num_segments_1 > 0:                
                    # this joint has absolute coordinates
                    joint_position = [0, self.torso_size[1]/2, self.torso_size[2]*1.5]
                    pyrosim.Send_Joint(name = "Torso_i"+str(n) , parent= "Torso" , child = "i"+str(n) , type = "revolute", position = joint_position, jointAxis = '1 0 0', rpy = random.randint(0,3))
        n = 0
        while n < self.num_segments_1:

            # Color coding cubes
            if self.cube_sensors_b1[n] == True:
                color_code = green_code
                color_name = green_name
            elif self.cube_sensors_b1[n] == False:
                color_code = blue_code
                color_name = blue_name

            # relative to previous joint
            cube_position = [self.cube_sizes_b1[n][0]/2,self.cube_sizes_b1[n][1]/2,self.cube_sizes_b1[n][2]/2]
            # cube_position = [np.random.uniform(-1,1)*size_dummy_1[0]/2,size_dummy_1[1]/2,np.random.uniform(-1,1)*size_dummy_1[2]/2]
            pyrosim.Send_Cube(color_code = red_code, color_name = red_name,name = "i"+str(n), pos=cube_position , size=self.cube_sizes_b1[n])
            if n < self.num_segments_1 - 1:
                # relative to previous joint
                pyrosim.Send_Joint(name = "i"+str(n)+'_'+ "i"+str(n+1), parent = "i"+str(n), child = "i"+str(n+1), type = "revolute", position = [0,self.cube_sizes_b1[n][1],0], jointAxis = "1 0 0", rpy = 1)
            n = n + 1
        

        # Branch 2 Links
        n = 0
        if self.num_segments_2 > 0:
            joint_position = [0, -self.torso_size[1]/2, self.torso_size[2]*1.5]
            pyrosim.Send_Joint(name = "Torso_j"+str(n) , parent= "Torso", child = 'j'+str(n) , type = "revolute", position = joint_position, jointAxis = "1 0 0", rpy = 3)

        n = 0
        while n < self.num_segments_2:
            
            # color coding links
            if self.cube_sensors_b2[n] == True:
                color_code = green_code
                color_name = green_name
            elif self.cube_sensors_b2[n] == False:
                color_code = blue_code
                color_name = blue_name
            #cube_position = [np.random.uniform(-1,1)*size_dummy_2[0]/2,-size_dummy_2[1]/2,np.random.uniform(-1,1)*size_dummy_2[2]/2]
            cube_position = [self.cube_sizes_b2[n][0]/2,-self.cube_sizes_b2[n][1]/2,self.cube_sizes_b2[n][2]/2]
            pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = "j"+str(n), pos=cube_position , size=self.cube_sizes_b2[n])
            if n < self.num_segments_2 - 1:
                # relative to previous joint
                pyrosim.Send_Joint(name = "j"+str(n)+'_'+ "j"+str(n+1), parent = "j"+str(n), child = "j"+str(n+1), type = "revolute", position = [0,-self.cube_sizes_b2[n][1],0], jointAxis = "1 0 0", rpy = 1)
            n = n + 1


        # Branch 3 Links
        n = 0
        if self.num_segments_3 > 0:
            joint_position = [0, 0, self.torso_size[2]*2]
            pyrosim.Send_Joint(name = "Torso_k"+str(n) , parent= "Torso", child = 'k'+str(n) , type = "revolute", position = joint_position, jointAxis = "1 0 0", rpy = 3)

        n = 0
        while n < self.num_segments_3:
            
            # color coding links            
            if self.cube_sensors_b3[n] == True:
                color_code = green_code
                color_name = green_name
            elif self.cube_sensors_b3[n] == False:
                color_code = blue_code
                color_name = blue_name
            # relative to previous joint
            #cube_position = [np.random.uniform(-1,1)*size_dummy_3[0]/2,size_dummy_3[1]/2,size_dummy_3[2]/2]
            cube_position = [self.cube_sizes_b3[n][0]/2,self.cube_sizes_b3[n][1]/2,self.cube_sizes_b3[n][2]/2]
            pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = "k"+str(n), pos=cube_position , size=self.cube_sizes_b3[n])
            if n < self.num_segments_3 - 1:
                # relative to previous joint
                pyrosim.Send_Joint(name = "k"+str(n)+'_'+ "k"+str(n+1), parent = "k"+str(n), child = "k"+str(n+1), type = "revolute", position = [0,0,self.cube_sizes_b3[n][2]], jointAxis = "1 0 0", rpy = 1)
            n = n + 1

        pyrosim.End()

    def Create_Brain(self):


        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        all_sensors = []

        numMotors = len(self.total_cubes)  # every joint will have a motor
        numSensors = len(self.sensor_cubes)

        ### need to remove self dependencies in brain so that its reproducible, but need the correct size of sensors and motors
        for i,sensor in enumerate(self.sensor_cubes):
            pyrosim.Send_Sensor_Neuron(name = i, linkName = sensor)
            all_sensors.append((i,sensor))

        # self.total_cubes.remove('Torso')
        self.total_cubes.sort()
        for j, motor in enumerate(self.joint_names):
            if motor == 'Torso':
                pass
            else:
                pyrosim.Send_Motor_Neuron(name = j + numSensors , jointName = self.joint_names[j])

        # all pairs of neurons must have synapses:
        for currentRow in range(numSensors):
            for currentColumn in range(numMotors):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + numSensors, weight = self.weights[currentRow][currentColumn])

        
        pyrosim.End()


    def Mutate(self):

        # # roll a die
        brain_body_coin = random.randint(0,2) # 0 means no change, 1 means chain body, 2 means change brain

        # change body
        if brain_body_coin == 1:
            
            add_remove_size = rand.randint(0,3)
            
            ### removal working
            if add_remove_size == 0: # remove a link
                print("Link Removed")
                body_coin = random.randint(1,3)
                if body_coin == 1 & self.num_segments_1 > 1:
                    self.num_segments_1 = self.num_segments_1 - 1
                    if self.cubes_b1[-1] in self.sensor_cubes:
                        self.sensor_cubes.remove(self.cubes_b1[-1])
                    if self.cubes_b1[-1] in self.total_cubes:
                        self.total_cubes.remove(self.cubes_b1[-1])
                    self.cubes_b1.remove(self.cubes_b1[-1])
                    
                    removal_index = []
                    for i in range(len(self.joint_names)):
                        if self.cubes_b1[-1] in self.joint_names[i]:
                            removal_index.append(i)
                    for val in reversed(removal_index):
                        self.joint_names.remove(self.joint_names[val])
                
                if body_coin == 2 & self.num_segments_2 > 1:
                    self.num_segments_2 = self.num_segments_2 - 1
                    if self.cubes_b2[-1] in self.sensor_cubes:
                        self.sensor_cubes.remove(self.cubes_b2[-1])
                    if self.cubes_b2[-1] in self.total_cubes:
                        self.total_cubes.remove(self.cubes_b2[-1])
                    self.cubes_b2.remove(self.cubes_b2[-1])
                    
                    removal_index = []
                    for i in range(len(self.joint_names)):
                        if self.cubes_b2[-1] in self.joint_names[i]:
                            removal_index.append(i)
                    for val in reversed(removal_index):
                        self.joint_names.remove(self.joint_names[val])
                
                if body_coin == 3 & self.num_segments_3 > 1:
                    self.num_segments_3 = self.num_segments_3 - 1
                    if self.cubes_b3[-1] in self.sensor_cubes:
                        self.sensor_cubes.remove(self.cubes_b3[-1])
                    if self.cubes_b3[-1] in self.total_cubes:
                        self.total_cubes.remove(self.cubes_b3[-1])
                    self.cubes_b2.remove(self.cubes_b2[-1])
                    
                    removal_index = []
                    for i in range(len(self.joint_names)):
                        if self.cubes_b3[-1] in self.joint_names[i]:
                            removal_index.append(i)
                    for val in reversed(removal_index):
                        self.joint_names.remove(self.joint_names[val])

            if add_remove_size == 1: # add a link
                print("Link Added")
                body_coin = random.randint(1,3)

                if body_coin == 1 and self.num_segments_1 < self.max_seg_size:

                    i = self.num_segments_1 # n will be value of cube
                    self.cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
                    self.cube_sizes_b1.append(self.cube_size_rand)
                    self.cubes_b1.append("i" + str(i))
                    self.total_cubes.append("i" + str(i))
                    self.joint_names.append("i"+str(i-1)+'_'+ "i"+str(i))
                    
                    cube_sense = random.choice((True,False))
                    self.cube_sensors_b1.append(cube_sense)
                    if self.cube_sensors_b1[i-1] == True:
                        self.sensor_cubes.append(self.cubes_b1[i-1])
                    self.num_segments_1 = self.num_segments_1 + 1
                
                if body_coin == 2 and self.num_segments_2 < self.max_seg_size:
                    i = self.num_segments_2 # n will be value of cube
                    self.cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
                    self.cube_sizes_b2.append(self.cube_size_rand)
                    self.cubes_b1.append("j" + str(i))
                    self.total_cubes.append("j" + str(i))
                    self.joint_names.append("j"+str(i-1)+'_'+ "j"+str(i))
                    
                    cube_sense = random.choice((True,False))
                    self.cube_sensors_b2.append(cube_sense)
                    if self.cube_sensors_b2[i-1] == True:
                        self.sensor_cubes.append(self.cubes_b2[i-1])
                    self.num_segments_2 = self.num_segments_2 + 1

                if body_coin == 3 and self.num_segments_3 < self.max_seg_size:
                    i = self.num_segments_3 # n will be value of cube
                    self.cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
                    self.cube_sizes_b3.append(self.cube_size_rand)
                    self.cubes_b3.append("k" + str(i))
                    self.total_cubes.append("k" + str(i))
                    self.joint_names.append("k"+str(i-1)+'_'+ "k"+str(i))
                                            
                    cube_sense = random.choice((True,False))
                    self.cube_sensors_b3.append(cube_sense)
                    if self.cube_sensors_b3[i-1] == True:
                        self.sensor_cubes.append(self.cubes_b3[i-1])
                    self.num_segments_3 = self.num_segments_3 + 1
            ## Change Size
            if add_remove_size == 3:
                print("Link Increased Size")
                # pick a random value in a branch
                # change the size \
                body_coin = random.randint(1,3)
                if body_coin == 1:
                    rand_n = random.randint(0,2)
                    for i in range(2):
                        self.cube_sizes_b1[rand_n][i] = self.cube_sizes_b1[rand_n][i] *1.1
                if body_coin == 2:
                    rand_n = random.randint(0,2)
                    for i in range(2):
                        self.cube_sizes_b2[rand_n][i] = self.cube_sizes_b2[rand_n][i] *1.1
                if body_coin == 3:
                    rand_n = random.randint(0,2)
                    for i in range(2):
                        self.cube_sizes_b3[rand_n][i] = self.cube_sizes_b3[rand_n][i] *1.1
            if add_remove_size == 4:
                body_coin = random.randint(1,3)
                print("Link Decreased Size")
                if body_coin == 1:
                    rand_n = random.randint(0,2)
                    for i in range(2):
                        self.cube_sizes_b1[rand_n][i] = self.cube_sizes_b1[rand_n][i] *.9
                if body_coin == 2:
                    rand_n = random.randint(0,2)
                    for i in range(2):
                        self.cube_sizes_b2[rand_n][i] = self.cube_sizes_b2[rand_n][i] *.9
                if body_coin == 3:
                    rand_n = random.randint(0,2)
                    for i in range(2):
                        self.cube_sizes_b3[rand_n][i] = self.cube_sizes_b3[rand_n][i] *.9
            
        # if brain_body_coin == 0:
            # add, remove sensor
            # add, remove synapse

        
