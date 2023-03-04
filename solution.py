import numpy as np
import numpy.random as rand
import random
import pyrosim.pyrosim as pyrosim
import os
import time
import constants as c


class SOLUTION:

    def __init__(self, nextAvailableID):
        
        self.weights = 0
        self.myID = nextAvailableID

        self.numMotors = 0
        self.numSensors = 0

        self.joint_names = []
        self.sensor_cubes = ['Torso']
        self.total_cubes = ['Torso']

        
        ### Initializing Cube Existence, Size, and Names
        self.cubes_b1 = []
        self.cubes_b2 = []
        self.cubes_b3 = []

        # self.num_segments_1 = random.randint(0,3)
        # self.num_segments_2 = random.randint(0,3)
        # self.num_segments_3 = random.randint(0,3)

        self.num_segments_1 = 2
        self.num_segments_2 = 1
        self.num_segments_3 = 1

        self.cube_sizes_b1 = []
        self.cube_sizes_b2 = []
        self.cube_sizes_b3 = []

        self.cube_names_b1 = []
        self.cube_names_b2 = []
        self.cube_names_b3 = []
        
        for i in range(self.num_segments_1):
            self.cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
            self.cube_sizes_b1.append(self.cube_size_rand)
            self.cube_names_b1.append("i"+str(i))
            self.total_cubes.append("i"+str(i))

        for i in range(self.num_segments_2):
            self.cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
            self.cube_sizes_b2.append(self.cube_size_rand)
            self.cube_names_b2.append("j"+str(i))
            self.total_cubes.append("j"+str(i))
        
        for i in range(self.num_segments_3):
            self.cube_size_rand =  [random.uniform(.2,1),random.uniform(.2,1),random.uniform(.2,1)]
            self.cube_sizes_b3.append(self.cube_size_rand)
            self.cube_names_b3.append("k"+str(i))
            self.total_cubes.append("k"+str(i))


        self.torso_size = np.zeros(3)
        for x in range(3):
            self.torso_size[x] = random.uniform(.3,1) * 1.3
        self.cube_sizes = random.uniform(.2,1) *.9

        ### Initializing Cube Names
        print(self.cube_names_b1)
        print(self.cube_names_b2)
        print(self.cube_names_b3)
        print(self.total_cubes)

        
        ### Initializing Cube Sensoring
        self.cube_sensors_b1 = []
        self.cube_sensors_b2 = []
        self.cube_sensors_b3 = []


        for i in range(self.num_segments_1):
            cube_sense = random.choice((True,False))
            self.cube_sensors_b1.append(cube_sense)
            # if self.cube_sensors_b1[i] == True:
            #     self.sensor_cubes.append(self.cube_sensors_b1[i])

        for i in range(self.num_segments_2):
            cube_sense = random.choice((True,False))
            self.cube_sensors_b2.append(cube_sense)
            # if self.cube_sensors_b2[i] == True:
            #     self.sensor_cubes.append(self.cube_sensors_b2[i])

        for i in range(self.num_segments_3):
            cube_sense = random.choice((True,False))
            self.cube_sensors_b3.append(cube_sense)
            # if self.cube_sensors_b3[i] == True:
            #     self.sensor_cubes.append(self.cube_sensors_b3[i])

        ### append everything up here
        ### make color arrays up here
    

      

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
                    self.joint_names.append('Torso_i'+str(n))
        n = 0
        while n < self.num_segments_1:
            self.cubes_b1.append('i'+str(n))
            #self.total_cubes.append(self.cubes_b1[n])

            # Color coding cubes
            if self.cube_sensors_b1[n] == True:
                color_code = green_code
                color_name = green_name
                self.sensor_cubes.append(self.cubes_b1[n])
            elif self.cube_sensors_b1[n] == False:
                color_code = blue_code
                color_name = blue_name

            # relative to previous joint
            cube_position = [self.cube_sizes_b1[n][0]/2,self.cube_sizes_b1[n][1]/2,self.cube_sizes_b1[n][2]/2]
            # cube_position = [np.random.uniform(-1,1)*size_dummy_1[0]/2,size_dummy_1[1]/2,np.random.uniform(-1,1)*size_dummy_1[2]/2]
            pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = "i"+str(n), pos=cube_position , size=self.cube_sizes_b1[n])
            if n < self.num_segments_1 - 1:
                # relative to previous joint
                pyrosim.Send_Joint(name = "i"+str(n)+'_'+ "i"+str(n+1), parent = "i"+str(n), child = "i"+str(n+1), type = "revolute", position = [0,self.cube_sizes_b1[n][1],0], jointAxis = "1 0 0", rpy = 1)
                self.joint_names.append("i"+str(n)+'_'+ "i"+str(n+1))
            n = n + 1
        

        # Branch 2 Links
        n = 0
        if self.num_segments_2 > 0:
            joint_position = [0, -self.torso_size[1]/2, self.torso_size[2]*1.5]
            pyrosim.Send_Joint(name = "Torso_j"+str(n) , parent= "Torso", child = 'j'+str(n) , type = "revolute", position = joint_position, jointAxis = "1 0 0", rpy = 3)
            self.joint_names.append("Torso_j"+str(n))

        n = 0
        while n < self.num_segments_2:
            self.cubes_b2.append('j'+str(n))
            #self.total_cubes.append(self.cubes_b2[n])
            
            # color coding links
            if self.cube_sensors_b2[n] == True:
                color_code = green_code
                color_name = green_name
                self.sensor_cubes.append(self.cubes_b2[n])
            elif self.cube_sensors_b2[n] == False:
                color_code = blue_code
                color_name = blue_name
            #cube_position = [np.random.uniform(-1,1)*size_dummy_2[0]/2,-size_dummy_2[1]/2,np.random.uniform(-1,1)*size_dummy_2[2]/2]
            cube_position = [self.cube_sizes_b2[n][0]/2,-self.cube_sizes_b2[n][1]/2,self.cube_sizes_b2[n][2]/2]
            pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = "j"+str(n), pos=cube_position , size=self.cube_sizes_b2[n])
            if n < self.num_segments_2 - 1:
                # relative to previous joint
                pyrosim.Send_Joint(name = "j"+str(n)+'_'+ "j"+str(n+1), parent = "j"+str(n), child = "j"+str(n+1), type = "revolute", position = [0,-self.cube_sizes_b2[n][1],0], jointAxis = "1 0 0", rpy = 1)
                self.joint_names.append("j"+str(n)+'_'+ "j"+str(n+1))
            n = n + 1


        # Branch 3 Links
        n = 0
        if self.num_segments_3 > 0:
            joint_position = [0, 0, self.torso_size[2]*2]
            pyrosim.Send_Joint(name = "Torso_k"+str(n) , parent= "Torso", child = 'k'+str(n) , type = "revolute", position = joint_position, jointAxis = "1 0 0", rpy = 3)
            self.joint_names.append("Torso_k"+str(n))

        n = 0
        while n < self.num_segments_3:
            self.cubes_b3.append('k'+str(n))
            #self.total_cubes.append(self.cubes_b3[n])
            
            # color coding links            
            if self.cube_sensors_b3[n] == True:
                color_code = green_code
                color_name = green_name
                self.sensor_cubes.append(self.cubes_b3[n])
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
                self.joint_names.append("k"+str(n)+'_'+ "k"+str(n+1))
            n = n + 1


        #print(self.sensor_cubes)

        self.numMotors = len(self.total_cubes)  # every joint will have a motor
        self.numSensors = len(self.sensor_cubes)

        self.weights = np.random.rand(self.numSensors, self.numMotors) * 2 - 1

        pyrosim.End()

    def Create_Brain(self):


        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        all_sensors = []
        all_motors = []
        
        for i,sensor in enumerate(self.sensor_cubes):
            pyrosim.Send_Sensor_Neuron(name = i, linkName = sensor)
            all_sensors.append((i,sensor))

        # self.total_cubes.remove('Torso')
        self.total_cubes.sort()
        for j, motor in enumerate(self.joint_names):
            # print(j, motor)
            # print('len joint names',len(self.joint_names))
            if motor == 'Torso':
                pass
            else:
                pyrosim.Send_Motor_Neuron(name = j + self.numSensors , jointName = self.joint_names[j])

        # all pairs of neurons must have synapses:
        for currentRow in range(self.numSensors):
            for currentColumn in range(self.numMotors):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + self.numSensors, weight = self.weights[currentRow][currentColumn])

        # print(self.cubes_b1)
        # print(self.cubes_b2)
        # print(self.cubes_b3)
        # print(self.joint_names)
        pyrosim.End()


    def Mutate(self):
      
        col = rand.randint(0,self.numMotors) - 1
        row = rand.randint(0,self.numSensors) - 1
        self.weights[row][col] = rand.random() * 2 - 1

        # roll a die
        brain_body_coin = random.randint(0,2) # 0 means no change, 1 means chain body, 2 means change brain

        # change body
        if brain_body_coin == 1:
            
            add_remove = rand.randint(0,1)
            change_size = rand.randint(0,1)
            
            ### removal working
            if add_remove == 0: # remove a link
                body_coin = random.randint(1,3)
                if body_coin == 1 & self.num_segments_1 > 1:
                    self.num_segments_1 = self.num_segments_1 - 1
                    if self.cubes_b1[-1] in self.sensor_cubes:
                        self.total_cubes.remove(self.cubes_b1[-1])
                    if self.cubes_b1[-1] in self.total_cubes:
                        self.sensor_cubes.remove(self.cubes_b1[-1])
                    self.cubes_b1.remove(self.cubes_b1[-1])
                
                if body_coin == 2 & self.num_segments_2 > 1:
                    self.num_segments_2 = self.num_segments_2 - 1
                    if self.cubes_b2[-1] in self.sensor_cubes:
                        self.total_cubes.remove(self.cubes_b2[-1])
                    if self.cubes_b2[-1] in self.total_cubes:
                        self.sensor_cubes.remove(self.cubes_b2[-1])
                    self.cubes_b2.remove(self.cubes_b2[-1])
                
                if body_coin == 3 & self.num_segments_3 > 1:
                    self.num_segments_3 = self.num_segments_3 - 1
                    if self.cubes_b3[-1] in self.sensor_cubes:
                        self.total_cubes.remove(self.cubes_b3[-1])
                    if self.cubes_b3[-1] in self.total_cubes:
                        self.sensor_cubes.remove(self.cubes_b3[-1])
                    self.cubes_b2.remove(self.cubes_b2[-1])

                    #     if add_remove == 1: # add a link
            #         body_coin = random.randint(1,3)
            #         if body_coin == 1 & self.num_segments_1 < 4:
            #             self.num_segments_1 = self.num_segments_1 + 1
            #             ## blah blah add
            #         if body_coin == 2 & self.num_segments_2 < 4:
            #             self.num_segments_2 = self.num_segments_2 + 1
            #             ## blah blah add
            #         if body_coin == 3 & self.num_segments_3 < 4:
            #             self.num_segments_3 = self.num_segments_3 + 1
            #             ## blah blah add

            ## Change Size


       
       
        ### EXTRA CODE that I might not need???    
    
        # ## Segment 1 First Link
        # n = 0
        # if self.num_segments_1 > 0:    
        #     if n == 0:
        #         print('n',n)
        #         # this joint has absolute coordinates
        #         joint_position = [0, self.torso_size[1]/2, self.torso_size[2]*1.5]
        #         pyrosim.Send_Joint(name = "Torso_i"+str(n) , parent= "Torso" , child = "i"+str(n) , type = "revolute", position = joint_position, jointAxis = '1 0 0', rpy = random.randint(0,3))
        #         # size_dummy is for the branch cubes
        #         size_dummy = np.zeros(3)
        #         for x in range(3):
        #             size_dummy[x] = random.uniform(0,1) * .9
        #         cube_position = [np.random.uniform(-1,1)*size_dummy[0]/2,size_dummy[1]/2,np.random.uniform(-1,1)*size_dummy[2]/2]
        #         pyrosim.Send_Cube(color_code = blue_code, color_name = blue_name,name = "i"+str(n), pos=cube_position , size=size_dummy)
        #         self.cubes_b1 = ['i'+str(n)]
        #         self.sensor_cubes.append(self.cubes_b1[0])
        #         self.chosen_cubes.append(self.cubes_b1[0])

        #         if self.num_segments_1 > 1:
        #         # sending joint from link 0 to link 1
        #             pyrosim.Send_Joint(name = "i"+str(n)+'_'+ "i"+str(n+1), parent = "i"+str(n), child = "i"+str(n+1), type = "revolute", position = [0,size_dummy[1],0], jointAxis = "1 0 0", rpy = 1)
            
        #     while n < self.num_segments_1:
        #         print('n'+str(n))
        #         size_dummy_1 = np.zeros(3)
        #         for x in range(3):
        #             size_dummy_1[x] = random.uniform(0,1) * .9
        #         # relative to previous joint
        #         cube_position = [np.random.uniform(-1,1)*size_dummy_1[0]/2,size_dummy_1[1]/2,np.random.uniform(-1,1)*size_dummy_1[2]/2]
        #         pyrosim.Send_Cube(color_code = blue_code, color_name = blue_name,name = "i"+str(n), pos=cube_position , size=size_dummy_1)
        #         if n < self.num_segments_1 - 1:
        #             # relative to previous joint
        #             pyrosim.Send_Joint(name = "i"+str(n)+'_'+ "i"+str(n+1), parent = "i"+str(n), child = "i"+str(n+1), type = "revolute", position = [0,-size_dummy_1[1],0], jointAxis = "1 0 0", rpy = 1)
        #         self.cubes_b1.append('i'+str(n))
        #         self.sensor_cubes.append(self.cubes_b1[n])
        #         self.chosen_cubes.append(self.cubes_b1[n])
        #         n = n + 1
            #     # size_dummy_2 = np.zeros(3)
        #     # for x in range(3):
            #     size_dummy_2[x] = random.uniform(0,1) * .9
            # cube_position = [np.random.uniform(-1,1)*size_dummy_2[0]/2,-size_dummy_2[1]/2,np.random.uniform(-1,1)*size_dummy_2[2]/2]
            # pyrosim.Send_Cube(color_code = green_code, color_name = green_name,name = "Leg2", pos=cube_position , size=size_dummy_2)
            # self.sensor_cubes.append('Leg2')
            # self.chosen_cubes.append('Leg2')
            # self.cubes_b2 = ['Leg2']
            # self.sensor_cubes.append(self.cubes_b2[0])
            # self.chosen_cubes.append(self.cubes_b2[0])

            # # relative to previous joint
            # size_dummy = np.zeros(3)
            # for x in range(3):
            #     size_dummy[x] = random.uniform(0,1) * .9   
            # pyrosim.Send_Joint(name = "Leg2_LowerLeg2", parent = "Leg2", child = "LowerLeg2", type = "revolute", position = [0,-size_dummy[1],0], jointAxis = "1 0 0", rpy = 1)
            # cube_position = [np.random.uniform(-1,1)*size_dummy[0]/2,-size_dummy[1]/2,np.random.uniform(-1,1)*size_dummy[2]/2]
            # pyrosim.Send_Cube(color_code = green_code, color_name = green_name,name = "LowerLeg2", pos=cube_position , size=size_dummy)



