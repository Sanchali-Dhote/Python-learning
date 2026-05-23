#tree is a nonlinear data structure with hierarchical relationships between 
#its elements without having any cycle, it is basically reversed
#representation of tree data structure: 1] linked list
#2]Python list (array)
class Tree:
    def __init__(self, data):
        self.data = data#("Drinks")
        self.child =[]

    def __str__(self, level = 0):
        ret =" "* level + str(self.data) + "\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret


    def addChild(self, object):
        self.child.append(object)
        print("Tree node added")
        
rootNode = Tree("Drinks")
Hot      = Tree("Hot")
Cold     = Tree("Cold")
Tea      = Tree("Tea")
Coffee   = Tree("Coffee")
NonAlchoholic = Tree("Non Alchoholic")
Alchoholic    = Tree("Alchoholic")

rootNode.addChild(Hot)#left
rootNode.addChild(Cold)#right
Hot.addChild(Tea)#left
Hot.addChild(Coffee)#right
Cold.addChild(NonAlchoholic)#left
Cold.addChild(Alchoholic)#right

print(rootNode)

#Array Rotation
#rotate an array to the right by a given number of steps
#sample input: [1,2,3,4]rotated by 2 steps
#sample output: [4,5,1,2,3]