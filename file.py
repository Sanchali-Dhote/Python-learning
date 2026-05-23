# import math #wipro
# mylist = [17,77,54,81,48,34,25,16]
# count = 0
# for i in range (len(mylist)):
#     root = int(math.sqrt(mylist[i]))
#     if root*root == mylist[i]:
#         count += 1
# print(count)
#================================================================================
#Q]
# def func(value, values):#[44,2,3]
#     var = 1
#     values[0] = 44

# t = 3
# v =[1,2, 3]
# func(t,v)
# print(t, v[0]) Ans: 3 44
#===================================================
#Q]
# def f(i, values = []):
#     values.append(i)
#     print (values)
#     #return values
# f(1)#calling function
# f(2)
# f(3) #ans: [1] [1,2] [1,2,3]
#===============================================================
#Queue DS
# 1.Enqueue
# 2.dequeue
# 3.display queue
# 4.isEmpty()
# 5.isFull()
# 6.Delete
# 7.peek()

# import sys
# class Queue:
#     def __init__(self, size):
#         self.myQueue =[] #creating stack
#         self.queueSize = size #stack size defined

#     def isFull(self):
#         if len(self.myQueue) == size:
#             return True
#         else:
#             return False
        
#     def enQueue(self,value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.myQueue.append(value)

#     def display(self):
#         print(self.myQueue)

#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False

#     def deQueue(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             self.myQueue.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print(self.myQueue[0])

#     def deleteQueue(self):
#         self.myQueue = None
    
# size = int(input("Enter the size of Queue :"))
# obj = Queue(size)
# print("Queue has created :")
# while True:
#     print("1. Enqueue Operation :")
#     print("2. Display Queue :")
#     print("3. deQueue Operation :")
#     print("4. Peek Operation :")
#     print("5. Delete Queue :")
#     print("6. Exit")
#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         value = int(input("Enter element to add in Queue: "))
#         obj.enQueue(value)

#     elif choice == 2:
#         obj.display()

#     elif choice == 3:
#         obj.deQueue()

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         obj.deleteQueue()

#     elif choice == 6:
#         sys.exit()
#===================================================================
#Stack using List
# -Easy to NotImplemented
# -Speed problem when it grows

# Stack usign linked list
# -fast performance
# -implementation is not easy

# create stack         TC=O(1)                       SC =O(1)
# push                 =O(1)/O(n^2)                   O(1)
# pop                  =O(1)                          O(1)
# peek                  O(1)                          O(1)
# isEmpty               O(1)                          O(1)
# delete entire stack   O(1)                          O(1)


# create queue                       O(1)                  O(1)
# enqueue                            O(n)                  O(1)
# dequeue                            O(n)                  O(1)
# peek                               O(1)                  O(1)
# isEmpty                            O(1)                  O(1)
# delete entire queue                O(1)                  O(1)

# *queue using list
# easy to Implement  
# speed problem when it grows

# *queue using linked list
# fast performance
# implementation is not easy

# fruit = {} #{'Apple':1,'Banana':1,'apple':1}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print (len(fruit))
#===========================================================================
#Write a program to accept student name and marks from the keyboard and creates a dictionary.
#ALso display student marks by taking student name
# n = int(input("Enter the number of students: "))#2
# d={}
# for i in range(n):
#     name=input("Enter Student Name: ")
#     marks=input("Enter Student Marks: ")
#     d[name]=marks #add key:value
# while True:
#     name=input("Enter Student Name to get Marks: ")
#     marks=d.get(name, -1)
#     if marks== -1:
#         print("Student Not Found")
#     else:
#         print("The Marks of",name,"are",marks)
#     option=input("Do you want to find another student marks[Yes|No]")
#     if option=="No":
#         break
# print("Thanks for using our application")
#==========================================================================    
#write a program to access each character of string in forward and backward direction 
#by using while loop?
#i/p="Learning Python is very easy"

# s = "Learning Python is very easy"

# n=len(s)
# i=0
# print("Forward Direction:")
# while i < n:#i=0
#     print(s[i], end="")
#     i += 1

# print("\nBackward Direction:")
# i = - 1
# while i >= -n:
#     print(s[i], end="")
#     i = i - 1
#===========================================
#input: abcdfjgerj abcdfjger
#output: j
# s = "abcdfjgerj abcdfjger"

# words = s.split()

# for ch in words[0]:
#     if words[0].count(ch) != words[1].count(ch):
#         print(ch)
#         break
#================================================================
# v=['a','e','i','o','u']
# w=input("Enter the word where we will search the vowels: ")
# #w=prashantjha
# found=[]#a
# for i in w:#i=2:a
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('found vowels=',found)
# print('Unique vowels',len(found), 'from the given word=',w)
#======================================================================
# x,y,z = map(int, input().split()) #x=6, y=30, z=50
# mylist =[] #29 38 12 48 39 55
# for i in range(x):
#     a = int(input())
#     mylist.append(a)
# for j in mylist: #j=3:48
#     if j>=y and j<=z:
#         print(j, end=' ')
#=====================================================
# import datetime
# #datetime formatting
# date=datetime.datetime.now()
# print("It's now:{:%d/%m/%Y %H/%M:%S}".format(date))
#====================================================
# x=['A','B','C']
# y=['A','B','C']
# z= [1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)
#ans ->True -> checking addresses not values
#False
#True
#==================================================
#s = [1,4,9,16,25,36,49,64,81,100]
# val=[2**i for i in range(1,6)]#i=1,2,3,4,5
# print(val)
#val2=[i for i in s if i%2==0]#i=1
#print(val2)
#ans ->[2, 4, 8, 16, 32]
#=======================================
# s=[i*i for i in range(1,11)]#i=4
# print(s)
#ans->[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#=================================================
# squares={x:x*x for x in range(1,6)}#x=4
# print(squares)
#ans->{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#============================================
# doubles={x:2*x for x in range(1,6)}
# print(doubles)
#ans->{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
#====================================================
#
# a,b=[int(x) for x in input("enter 2 numbers :").split()]
# print("Product is :",a*b)
#ans->enter 2 numbers :4 6
#Product is : 24
#========================================================
# a,b,c=[float(x) for x in input("Enter 3 float numbers :").split(',')]
# print("The Sum is :", a+b+c)
#ans->Enter 3 float numbers :1.2, 2.2, 4.5
#The Sum is : 7.9
#========================================================
#we can use else block with for loop in python
# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("you have purchased everything")
#=====================================================
# username = "admin"
# password = "admin"

# Enter username
# Enter password

# right_username = "admin"
# right_password = "admin"

# username =""
# password = ""
# while username != right_username and password != right_password:
#         username = input("enter username: ")
#         password = input("enter password: ")
        
# print("login successfully")
#===============================================================================
#Tower of hanoi
import time
class Tower:
    def __init__(self):
        print("WELCOME TO TOWER OF HANOI GAME")
        print()
        print("Given Problem  A= [3,2,1]  B= []  C[] ")
        print()
        print("Expected Output A= []      B= []  C[3,2,1] ")
        self.A = []
        self.B = []
        self.C = []

    def tower(self,item):#item = 3
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items i Tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2)#A=[3,2]
        self.C.append(self.temp)#c=[1]=>temp=1
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B  ,"  ","C=",self.C)
        print("Pass one Completed==========================\n")

    def pass2(self):
        self.temp = self.A.pop(1)#
        self.B.append(self.temp)#B=[2]=>temp=2
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B  ,"  ","C=",self.C)
        print("Pass two Completed==========================\n")
    
    def pass3(self):
        self.temp = self.A.pop(0)#C=[]
        self.B.append(self.temp)#B=[2,1]
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B  ,"  ","C=",self.C)
        print("Pass three Completed==========================\n")

    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B  ,"  ","C=",self.C)
        print("Pass four Completed==========================\n")
    
    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B  ,"  ","C=",self.C)
        print("Pass five Completed==========================\n")
    
    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B  ,"  ","C=",self.C)
        print("Pass six Completed==========================\n")
    
    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B  ,"  ","C=",self.C)
        print("Pass seven Completed==========================\n")

t = Tower()
t.tower(3)
t.tower(2)
t.tower(1)
t.pass1()
t.pass2()
t.pass3()
t.pass4()
t.pass5()
t.pass6()
t.pass7()




    

