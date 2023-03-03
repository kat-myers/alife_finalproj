#generate from manylinks
import pyrosim.pyrosim as pyrosim
import numpy.random as rand

def Create_World():
	length=1
	width=1
	height=1

	x=3
	y=3
	z=0.5

	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name = "Torso", pos=[x,y,z] , size=[width, length, height])
	pyrosim.End()

def Generate_Body():
    length=1
    width=1
    height=1
    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name = "Torso", pos=[1, 0, 1.5] , size=[width, length, height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5, 0, 1.0])
    pyrosim.Send_Cube(name = "BackLeg", pos=[-0.5,0,-0.5] , size=[width, length, height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1.5,0,1])
    pyrosim.Send_Cube(name = "FrontLeg", pos=[0.5, 0, -0.5] , size=[width, length, height])

    pyrosim.End()


def Generate_Brain():

	pyrosim.Start_NeuralNetwork("brain.nndf")

	pyrosim.Send_Sensor_Neuron(name=0, linkName = "Torso")
	pyrosim.Send_Sensor_Neuron(name=1, linkName = "BackLeg")
	pyrosim.Send_Sensor_Neuron(name=2, linkName = "FrontLeg")
	


	pyrosim.Send_Motor_Neuron(name=3, jointName = "Torso_BackLeg"),
	pyrosim.Send_Motor_Neuron(name=4, jointName = "Torso_FrontLeg")

	# pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 3, weight  = 1)
	# pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 3, weight = 1)
	# pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 3, weight = 1)

	# pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 4, weight = 1)
	# pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 4, weight = 1)
	# pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 4, weight = 1)


	sensor_names = [0,1,2]
	motor_names = [3,4]
	weight = 1
	a = -1
	b = 1
	for s in sensor_names:
		for m in motor_names:
			pyrosim.Send_Synapse(sourceNeuronName = s, targetNeuronName = m, weight = a + (b-a)*rand.rand())



	pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()








	# pyrosim.Send_Cube(name = "BackLeg", pos=[0.5,0,0.5] , size=[width, length, height])

	# pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" , type = "revolute", position = [1, 0, 1.0])


	# pyrosim.Send_Cube(name = "Torso", pos=[0.5, 0, 0.5] , size=[width, length, height])

	# pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1,0,0])

	# pyrosim.Send_Cube(name = "FrontLeg", pos=[0.5, 0, -0.5] , size=[width, length, height])

# try with no torso as root
   
    




# def Create_Robot():
#     length=1
#     width=1
#     height=1
#     pyrosim.Start_URDF("body.urdf")
    
#     pyrosim.Send_Cube(name = "Torso", pos=[1, 0, 1.5] , size=[width, length, height])
#     pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5, 0, 1.0])
#     pyrosim.Send_Cube(name = "BackLeg", pos=[-0.5,0,-0.5] , size=[width, length, height])
#     pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1.5,0,1])
#     pyrosim.Send_Cube(name = "FrontLeg", pos=[0.5, 0, -0.5] , size=[width, length, height])
#     pyrosim.End()




#for i in range(10):
#	if i==0:
#		pyrosim.Send_Cube(name = "Box" + str(i), pos=[0,0,0.5+i] , size=[1, 1, 1])

#	else:
#		pyrosim.Send_Cube(name = "Box" + str(i), pos=[0,0,0.5+i] , size=[0.9**i, 0.9**i, #0.9**i])
	

