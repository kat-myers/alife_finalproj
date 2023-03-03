import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
	def __init__(self, linkName):
		self.linkName = linkName
		self.values = np.zeros(c.num_iters)
		#print(self.values)

	def Get_Value(self,t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		#if t == c.num_iters-1:
		#	print(self.values)

	def Save_Values(self):
		np.save('data/sensorValues.npy',self.values)