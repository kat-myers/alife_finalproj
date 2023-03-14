
# Kat Myers Final Project: The Artist
## Preview and Results
Below is a teaser gif of my robots, as well as some example runs of generations between 25-100, with populations of 10 each:
![teaser_gif](https://user-images.githubusercontent.com/122335561/225135264-a2b23bf2-a857-40f1-8a2a-142303c2b120.gif)


![example](https://user-images.githubusercontent.com/122335561/225115261-3bdf255d-132b-4afe-9d8f-265583b7eee7.png)
The fitness that I evaluated was the distance that the robots were able to move away in the negative y-direction. We can see that, for most of the simulation, very little successful evolution occcurs. The fitness curves plateau because, after a certain optimum is reached, any subsequent mutation is most likely to be deleterious than beneficial. However, occasionally, a positive mutation occurs. 

Over time, I think that the biggest impact in movement was the sensor location and the motor weight. It did not really matter where the cubes were located as long as some appendage cubes were touching and sensing the ground, and could therefore control when the motor responded. This resulted in more coordinated movement, rather than the random jerking around that could be seen in unevolved robots. Additionally, changing motor weights allowed for movement coordination as well. 

I think a big hindrance in my evolved robots were that, they could be great for movement given one very specific orientation, but if there was the slightest overexertion from a motor, then the robot would flip or change orientation and suddenly couldn't move. So even though a robot could be highly designed to move well, they were prone to poor performance because they couldn't stay flat on the ground, like a car that tends to flip over. I think I could change this by making the torso somehow heavier than the rest of the body, so that this center of mass would be harder for an individual joint motor to flip. 
For example, this seal-like creature only worked when he fell over and moved on his flippers, but just randomly jerked around until that happened

![def_evo_gif](https://user-images.githubusercontent.com/122335561/225124402-06b7bed8-f053-4b0b-b99a-8772404988fe.gif)

## Here is a link to a preview video:
https://youtu.be/r3AXp2UNxFo


## Background
## How Creatures Are Generated
### This code is found in the solution.py file
In this project, I create 3D, randomly-generated creatures. Each creature consists of a root link, called a torso, and has the opportunity to 
generate 0 to 3 segments coming from each branching point from the torso. The creatures can have 0 to n branching points, which are connected via joints at random
values along the face of the torso. A diagram for how these creatures are generated is shown below:
![A7_Creature_Generation](https://user-images.githubusercontent.com/122335561/220019495-a9e14a35-746b-4593-9f92-f7327993776e.png)
(inspiration for diagram from Karl Sims)

![IMG_0047](https://user-images.githubusercontent.com/122335561/220421421-a27ecf51-5b58-4ecf-8df8-dacae1fefaa6.jpg)

Each branch's segments are random sizes between .2 and 1, and are connected via joints at random points on the previous segment's face. The joints 
have been modified so that they can now be generated diagonally using "roll-pitch-yaw" arguments passed when the joint is defined.

Each of these joints has a motor neuron, and each link has a 50% chance of gaining a sensor neuron.
Links without sensors are blue, and links with sensor are green. An example is below:

![snake](https://user-images.githubusercontent.com/122335561/220019630-9309cda5-def3-428e-beac-4a1d2ed5f204.JPG)

The creatures are also generated to minimize intersection with other segments. Adjacent cubes are allowed to intersect, but nonadjancent cubes or cubes from different
branches are stopped from doing so by checking that the next generated cube will not generate into a position where a cube already exists

## The Genotype
<img width="918" alt="genotype info diagram" src="https://user-images.githubusercontent.com/122335561/225096026-36d7e026-6ba0-4a12-9592-1b421de48fd2.png">
The gentype is translated into the phenotype through the use of my Create_Body and Create_Brain functions
Each branch is created using the information in the genotype, where each link on the branches are then created and their joints relative to the previous joints are written

## The Body
The creature's individual links are rectangular prisms with any dimension randomly varying from .2 to 1. 
Movements are based on revolute joints with varying axes that can operated at angles with the addition of the "roll-pitch-yaw" argument I added in "Send_Joint"
Below are some possible bodies that could be generated:

![mark_rothko](https://user-images.githubusercontent.com/122335561/225096680-7f25a210-4907-49a0-8cae-df19f3a28928.png)
![mr_krabs](https://user-images.githubusercontent.com/122335561/225096715-d24190cf-b670-4ec9-ace6-04a867c28aa7.png)

## The Brain

Each creature's joints contain a motor neuron, and each link has a 50% chance of containing a sensor neuron. Within each branch from the torso root link, all motor
and sensor neurons are connected via synapses. However, no connections are present between the different branches in this iteration. This allows for isolated
bevahior within each branch, which might make coordinated movement more difficult for my creatures.

## Evolution
The creatures are given an opportunity to evolve. This is done by beginnning a population
with randomly generated creatures, and evaluating the fitness, defined as the ability of the
creatures to move in the y direction:
   stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[1]
        yCoordinateOfLinkZero = positionOfLinkZero[1]
The creatures with the highest fitness are then randomly mutated and allowed to evolve, seeding
the next generation. 
Mutations are performed when the parent replicates and passes its genotype to the child. I do this by making the child a copy of the parent, and then mutate the body or the brain. To mutate the body, I first flip a random coin between 0 and 2. If the value is 0, no mutation occurs, if it is 1, the body is mutated. If it is 2, the brain is mutated.
If the body is mutated, another coin chooses if a segment is added, removed, or changes size. Once this mutation type is determined, a segment on a branch is randomly pulled, and the mutation is made to the genotype before the new creature is created. Below is a diagram of possible mutations:
<img width="1050" alt="mutation diagram" src="https://user-images.githubusercontent.com/122335561/225100028-1bf600e4-79b1-4728-8a1b-52146cd53f9a.png">

## The Parallel Hill Climber
### this code is found in the parallelHillClimber.py file
The parallel hill climber enables us to run the simulation over multiple generations with different populations moving, reproducing, and evolving in parallel. It seeds a simulation with the set population and their genotypes, then evolves them by calling the mutation function for each child. After the children are created, the fitness of a parent and child pair is compared. If the child was able to move farther than the parent, then the child reproduces, and the parent does not, or vice versa. The parallel hill climber also saves the best fitnesses of each generation to a text file for the creation of growth curves.
<img width="1061" alt="PHC" src="https://user-images.githubusercontent.com/122335561/225103978-038e35a2-4b1d-482a-a287-712d49835563.png">


This is repeated for a certain number of generations with a certain population
size in each, defined in my constants.py file.
   

## How to Run
To run this simulation, clone my directory, fetch this branch, and run "py search.py" in your terminal :)
Enjoy!!
   
This project is part of CHE 396: Artificial Life, taught by Dr. Sam Kriegman at Northwestern University, Winter 2023
