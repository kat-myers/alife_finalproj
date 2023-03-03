import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
import sys

from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()




#physicsClient = p.connect(p.GUI)
# # motor command vector
# angle_range = np.linspace(0, 2*np.pi, c.num_iters)
# targetAngles_BackLeg = c.amplitude_BackLeg * np.sin(c.frequency_BackLeg * angle_range + c.phaseOffset_BackLeg)
# targetAngles_FrontLeg = c.amplitude_FrontLeg * np.sin(c.frequency_FrontLeg * angle_range + c.phaseOffset_FrontLeg)
# #np.save('data/targetAngles_BackLeg.npy', targetAngles_BackLeg)
# #np.save('data/targetAngles_FrontLeg.npy', targetAngles_FrontLeg)


# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)

# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)
# backLegSensorValues = np.zeros(c.num_iters)
# frontLegSensorValues = np.zeros(c.num_iters)



# for i in range(c.num_iters):
# 	p.stepSimulation()

# 	#backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	#print(backLegTouch)

	
# 	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_BackLeg", 
# 	controlMode = p.POSITION_CONTROL,targetPosition = targetAngles_BackLeg[i] ,maxForce = c.force)

# 	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_FrontLeg", 
# 	controlMode = p.POSITION_CONTROL,targetPosition = targetAngles_FrontLeg[i] ,maxForce = c.force)

# 	time.sleep(c.sleep_time)
# 	#print(i)

# #print(backLegSensorValues)
# np.save('data/backLegSensorValues.npy',backLegSensorValues)
# np.save('data/frontLegSensorValues.npy',frontLegSensorValues)
# p.disconnect()
