import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class MOTOR:
	def __init__(self, jointName):
		self.jointName = jointName
		self.motorValues =  np.zeros(c.num_iters)
		

	def Set_Value(self, jointName, desiredAngle):
		#print('joint', self.jointName)

		#t = desiredAngle

		# of just (desiredAngle = )
		desiredAngle = pyrosim.Set_Motor_For_Joint(bodyIndex = self.robotId,jointName = jointName, 
		controlMode = p.POSITION_CONTROL,targetPosition = desiredAngle ,maxForce = c.force)
		#targetPosition = robot.targetAngles2[t]

			#print('target angles2')
		 #changing targetAngles so one is 1/2 the other
		# else:
		# 	self.motorValues[t] = pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robotId,jointName = self.jointName, 
		# 	controlMode = p.POSITION_CONTROL,targetPosition = robot.targetAngles[t] ,maxForce = c.force)

		

		 	