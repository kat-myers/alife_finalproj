import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class WORLD:
    def __init__(self):

        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
        
    


        #physicsClient = p.connect(p.GUI)
        #p.connect(p.DIRECT)