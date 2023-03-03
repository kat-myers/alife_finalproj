from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL: 

    def __init__(self, color_code, color_name):

        self.depth  = 3

        self.string1 = color_name
        # original  '<material name="Cyan">'


        self.string2 = color_code # 0 1 1 1 for blue, 0 1 0 1 for green
        # original '<color rgba="0 1.0 1.0 1.0"/>'

        self.string3 = '</material>'

    def Save(self,f):
        #pass
        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
