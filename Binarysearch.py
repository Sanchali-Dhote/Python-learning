#binary search is faster than linear search
#half of the remaining elements can be eliminted at a time, instead of eliminating them one by one
#Binary search only works for sorted arrays.
# time complexity:O(logn)
# def binarySearch(array, target):
#     low = 0
#     high = len(array)-1
#     while low <= high:
#         mid = (low+high)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             low = mid+1
#         else:
#             high = mid - 1
#     return -1
# array =[2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target = 72
# result = binarySearch(array, target)
# if result == -1:
#     print("Element not found")
# else:
#     print("Element found at ",result)
#===========================================================================================
# def bubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):#j=1
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#             print(array)
#         print()

# array =[64, 34, 25, 12, 22, 11, 90]
# bubbleSort(array)
#=======================================================================
# mylist = [5,7,8,3,7,8,9,2,3]
# newlist=[]#7

# for i in range(len(mylist)):
#     count=0
#     key=mylist[i]#key=7
#     j=i+1 #j=3
#     while j<len(mylist):
#         if key == mylist[j]: #7 == 7
#             newlist.append(key)
#         j = j+1
# print(len(newlist))

#stack implementation without size limit
#stack implementation with size limit
#there are two ways 
#1]list/array
#2]inkedlist
#role of data members :represent strored data
# class Name:
#     age = 30 #data member
#     def display(self): #method
#         print("Hello world")

# obj = Name() #object is also called as reference variable
# print(obj.age)
# obj.display()

# class Student:
#     def __init__(self):
#         self.name = "sanchali"
#         self.age = 22

#     def display(self):
#         print("Name= ", self.name)
#         print("Age= ",self.age)

# stuObj = Student()
# print(stuObj)
    
    



# class Message:
#     def __init__(self):
#         print("I am constructor")
       
#     def shows(self):
#         print("Class program")
# obj = Message()
# obj.shows()
# obj2  = Message()
     
#parameterize constructor
# class StudentInfo:
#     def __init__(self, name, age, roll_no):
#         self.Name = name
#         self.Age = age
#         self.RollNo = roll_no
#     def displayStudentInfo(self):
#         print("Name=", self.Name)
#         print("Age=",self.Age)

# studentObj = StudentInfo("sanchali",22,41)
#======================================================
#Stack implementation

# import sys
# class Stack:
#     def __init__(self, size):
#         self.myStack =[] #creating stack
#         self.stackSize = size #stack size defined

#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#              return True
#         else:
#              return False

#     def push(self, value):
#         if self.isFull():
#              print("stack is full")
#         else:
#             self.myStack.append(value)
#             print("Element push")

#     def display(self):
#         print(self.myStack)

#     def isEmpty(self):
#         if self.myStack == []:
#               return True
#         else:
#               return False
  
#     def pop(self):
#         if self.isEmpty():
#             return len(self.myStack) == self.stackSize
#         else:
#             print(self.myStack.pop())

#     def peek(self):  #returns last operator first
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.myStack[-1])
    
#     def deleteStack(self):
#          self.myStack = None
# size = int(input("Enter the size of stack :"))
# obj = Stack(size)
# print("Stack has created :")
# while True:
#         print("1.Push Operation : ")
#         print("2.display stack: ")
#         print("3. Pop Operation: ")
#         print("4 Peek Operation: ")
#         print("5 Delete Stack: ")
#         print("7.Exit")
#         choice = int(input("Enter Your choice : "))
#         if choice == 1:
#             value  = int(input("Enter value to push in stack : "))
#             obj.push(value)
#         elif choice == 2:
#             obj.display()
#         elif choice == 3:
#             obj.pop()
#         elif choice == 4:
#             obj.peek()
#         elif choice == 5:
#             obj.deleteStack()
#         elif choice == 6:
#             obj.isEmpty()
#         elif choice == 7:
#             obj.isFull()
#         else:
#             sys.exit(0)
#=======================================================
#Stack implementation wihtout size limit 
#Stack implemetation 
#1.List/Array
#2.LinkedList
#Now you have to implement stack with size limit
#---------------------------------------------------
#1.Push
#2.Pop
#3.peek
#4.isEmpty
#5.isFull
#6.Delete
#7.display
mylist = [5,7,2,3,7,8,2,3,3]
newdict={}
for i in range(len(mylist)):
    count=0
    key=mylist[i]
    j =1
    while j<len(mylist):
        if key == mylist[j]:
            count+=1
        j = j+1
    if count>1:
        newdict[key]=count
max =newdict
print(max)
