#types of BT
#Full, complete, perfect, balanced
#1]Full Binary Tree: 1)each node has either 0 or 2 children
#2)No node has a single child

#2]Complete Binary Tree :1)All levels except possibly the last are completely filled
#2)Nodes in the last level are filled from left to right

#3]Perfect Binary Tree: 1)All internal nodes have exactly two nodes
#2)All leaf nodes are at the same level

#4]balanced

#Creation of tree
#insertion of a node
#deletion of a node
#search for a value
#traverse all nodes
#deletion of tree

#n1,n2,n4,n9,n10,n5,n3,n6,n7

#Preorder 
#inorder
#postorder
#these three are the type of depth first search

#why binary search tree:-
#it performs faster than  binary tree when inserting and deleting nodes

# class BSTNode:
#     def __init__(self, data):
#         self.data = data #(50)
#         self.leftChild = None
#         self.rightChild = None



# def insertNode(rootNode, nodeValue):#(50)
#     if rootNode.data == None:
#         rootNode.data = nodeValue
#     elif nodeValue <= rootNode.data:
#         if rootNode.leftChild is None:
#             rootNode.leftChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.leftChild, nodeValue)
#     else:
#         if rootNode.rightChild is None:
#             rootNode.rightChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.rightChild, nodeValue)

# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     print(rootNode.data,end=" ")
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)

# def inOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data,end=" ")
#     inOrderTraversal(rootNode.rightChild)

# def postOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data,end=" ")

# def searchNode(rootNode, nodeValue):
#     if rootNode.data == nodeValue:
#         print("The value is found")
#     elif nodeValue < rootNode.data:
#         if rootNode.leftChild ==  nodeValue:
#             print("The value is found")
#         else:
#             searchNode(rootNode.leftChild, nodeValue)
#     else:
#         if rootNode.rightChild.data == nodeValue:
#             print("The value is found")
#         else:
#             searchNode(rootNode.rightChild, nodeValue)


# newBST = BSTNode(None)
# insertNode(newBST, 70)
# insertNode(newBST, 50)
# insertNode(newBST, 90)
# insertNode(newBST, 30)
# insertNode(newBST, 60)
# insertNode(newBST, 80)
# insertNode(newBST, 100)
# insertNode(newBST, 20)
# insertNode(newBST, 40)
# insertNode(newBST, 10)
# preOrderTraversal(newBST)
# print()
# inOrderTraversal(newBST)
# print()
# postOrderTraversal(newBST)
# print()
# searchNode(newBST, 40)


#what is exception handling 
#what is types of error ? what is runtime error?
#what is syntax error
#we can take multiple exceptions in single exception block
# try:
#      a = int(input("Enter first number :"))
#      b = int(input("Enter second number :"))
#      print(a/b)
# except ZeroDivisionError:
#     print("invalid")
# except ValueError:
#     print("can't devide by zero")
# except:
#     print("ABC")
#========================================================
try:
     a = int(input("Enter first number :"))
     b = int(input("Enter second number :"))
     print(a/b)
except ZeroDivisionError:
    print("can't devide by zero")
except ValueError:
    print("Enter only integer value :")
else:
    print("I always executed")


   