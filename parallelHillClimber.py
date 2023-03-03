from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        if os.path.exists('brain*.nndf'):
            os.remove('brain*.nndf')
        if os.path.exists("fitness*.txt"):
            os.remove("fitness*.txt")
        if os.path.exists('body*.urdf'):
            os.remove('body*.urdf')
        if os.path.exists('bestfitness.txt'):
            os.remove('bestfitness.txt')
        
        
        #os.system('rm fitness*.txt')

        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            


        #self.child = SOLUTION()
        


    def Evolve(self):

        self.Evaluate(self.parents)   

        for currentGeneration in range(c.numberOfGenerations):
            print('currgen',currentGeneration)
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}

        for i,key in enumerate(self.parents):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    
    def Mutate(self):
        for i,key in enumerate(self.children):
            self.children[i].Mutate()
  
    def Evaluate(self, solutions):

        for i,key in enumerate(solutions):
            solutions[i].Start_Simulation("DIRECT")

        for i,key in enumerate(solutions):
            solutions[i].Wait_For_Simulation_To_End()
        

    def Select(self):
        for i,key in enumerate(self.parents):
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]
        
       


    def Print(self):
        #for i,key in enumerate(self.parents):
            #print('\n',i, self.parents[i].fitness, self.children[i].fitness,'\n')

         # identify lowest fitness to save
        best_fitness = 5
        for i,key in enumerate(self.parents):
            if self.parents[i].fitness < best_fitness:
                best_fitness = self.parents[i].fitness
            if self.children[i].fitness < best_fitness:
                best_fitness = self.children[i].fitness


        

        bestFitnessFileName = 'bestfitness.txt'
        f = open(bestFitnessFileName, 'a')
        f.write(str(best_fitness) + '\n')




        # tmpFileName = 'tmp' + str(self.solutionID) + '.txt'
        # fitnessFileName = 'fitness' + str(self.solutionID) + '.txt'
        # f = open(tmpFileName, 'w')
        # os.system('mv ' + tmpFileName + ' ' + fitnessFileName)
        # f.write(str(xCoordinateOfLinkZero))
        # f.close()




    def Show_Best(self):
        # find parent with the lowest fitness
        best_fitness = 5
        best_parent_ind = 0
        #print(self.parents[0])
        for i,key in enumerate(self.parents):
            curr_fitness = self.parents[i].fitness
            if curr_fitness < best_fitness:
                best_parent_ind = i
                #best_fitness = curr_fitness

        best_parent = self.parents[best_parent_ind]
        best_parent.Start_Simulation("GUI")



       #self.parent.Evaluate("GUI")



