import numpy as np
import matplotlib.pyplot as mp 

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
#print(backLegSensorValues)

# target angles
targetAngles_BackLeg = np.load("data/targetAngles_BackLeg.npy")
targetAngles_FrontLeg = np.load("data/targetAngles_FrontLeg.npy")

mp.plot(targetAngles_BackLeg, label = 'target angles back leg')
mp.plot(targetAngles_FrontLeg, label = 'target angles front leg', linewidth=4)

#mp.plot(targetAngles, label = 'target angles', linewidth=4)
#mp.plot(backLegSensorValues, label = 'back leg sensor values', linewidth=4)
#mp.plot(frontLegSensorValues, label = 'front leg sensor values')
mp.legend()
mp.show()