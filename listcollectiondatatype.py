# mylist = ["prashant", "Ashish","komal","ankush","Ashish",77,"sandip",60.52,"prashant"]
# # print(mylist)
# print(type(mylist))#<List>
# print(mylist[0])#prashant
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])#n=5,n-1=4 komal, ankush, ashish
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])#1,3,5,7,....
# mylist[2]="Akshay"
# print(mylist)
#========================================================
# if "ankush" in mylist:
#     print("yes ankush is available")
# else:
#     print("not available")
#============================================================
#append function always add Value at top
# mylist.append('harsh')
# mylist.append("laxman")
# print(mylist)

#add value at particular position
# mylist.insert(3,"sanket")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# newlist = mylist.copy() #cloning
# print(newlist)
# mylist = [['prashant', 'jha'],['85.56'],[440022,"yyy"]]
# print("example of multidimentional list: ")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0])#prashant
# print(mylist[0][1])#jha
# print(mylist[1][0])#85.56
# print(mylist[2][0])#440022
# print(mylist[2][1])#yyy
#-----------------------------
# list2 =[50,25.50,'prashant']
# del list2[2]
# #del list2
# print(list2)
#=================================
# list2=[50,25.50,'prashant']
# list2.clear()
# print(list2)

# name="prashant"
# print(name)
# myname=list(name)
# print(myname)

# mylist=[44,22,77,0,9,88]
# mylist.sort()
# #mylist.sort(reverse=True)#for descending order
# print(mylist)
# default sorting order for number is ascending order default sorting order for string is alphabetical order we should know that list should contain homogenious data 
# python2

#Alising meansassigning one variable reference to another variable
# mylist=[44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# mylist=[44,22,77,0,9,88]
# for i in mylist:#i=6
#     print(i)

#i/p = [0,1,4,0,2,5]
#o/p =[1,4,2,5,0,0]
#move the zero in last

# list1 = [0, 1, 4, 0, 2, 5]
# for i in list1:#i=3:0
#     if i == 0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)

# list1 = [7, 3, 9, 2, 8]
# list1.sort()
# print(list1[-2])
#===============================================================
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# a=[1,2,3,4,5]
# print(a[3:0:-1])

# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4):#i=4 #only focused on your row's
#     print(arr[i].pop())
#=================================================================
# fruit_list1 = ['Apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
#====================================================================
# sum = 0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)
#===============================================================
#find the intersection of three arrays:
#questions: find the common elements in three arrays.
#logic: Use three sets to keep track of common elements between the arrays.
#sample input: [1,2,3], [2,3,4], [3,4,5]
#expected output:[3]
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]

# for i in A:#i=2:3
#     if i in B and i in C:
#         print(i)
#=================================================================
# mylist = []
# N = int(input("Enter the value of N :"))#5
# for i in range(N):
#     val = int(input("Enter the value: "))
#     mylist.append(val)
# print(len(mylist))
# sum =0 #5
# for i in range(len(mylist)-1):#i=1
#     if i+1 in range(len(mylist)):
#         sum += abs(mylist[i]-mylist[i+1])#11 -7 =4
# print(sum)
#===============================================================
#13/05/2026
# name = "prashantjha"#this is our string 
# #012345678910
# print(name[0])#p
# print(name[1])#r
# print(name[-1])#a
# print(name[1:5])
# print(name[0:5])#end -1,5-1=4 prash
# print(name[1:])#rashantjha
# print(name[:5])#5-1=4 prash
# print(name[:])#prahshantjha
# print(name[1:8:2])#'''8-1=7=rsat
# print(name[::-1])#reverse of string
#============================================================
# s = "Python are High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())
#===========================================================
# name = "prashant"
# sal= 5000
# age = 28
# print("{} sal is {} age is{}".format(name,sal,age))
# print("{0} sal is {1} age is {2}".format(name,sal,age))
# print("{x} sal is {y} age is{z}".format(x=name,y=sal,z=age))
# A=1
# print(f"{A} is a good boy")
#============================================================
# name = "prashant"
# for i in name: #i=0:p
#     print(i)

#i/p=prashant
#o/p=prashnt
#WAP to remove duplicate char
# name = "sanchali"
# newname = ""
# N = len(name)#8-1=7
# for i in range(N-1, -1, -1):#i=7
#         newname += name[i]
# print(newname)
#================================================================
#check for palindrome
# name = "racecar"
# name = "help4code"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("palindrome")
# else:
#     print("Not palindrome")

#count vowels and consonants
#wAP to count the number of vowels and consonants in a given string
#sample input = "hello"
# vowels =['a','e','i','o','u']
# name = "hello"
# cons =0 #1
# vow =0#
# for i in name:#i=4:o
#     if i in vowels:
#         vow += 1
#     else:
#         cons +=1
# print("consonent =",cons)
# print("vow ",vow)
#=========================================================================
#check for anagram
# WAP to check if two string are anagrams of each other.
# logic: check if the character counts in both strings are the same
# sample input: "listen" and "silent"
# output: Anagram
#===========================================================================
#count words in a string
#WAP to count the number of words in a string
# logic: use loops to count spaces and words
# sample input "THis is a sentence"
# output: 4
#==============================
# a = 50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
#===============================================================
# s = "this is a test"
# print(s.title())
#=======================================================
# print('prashantjha777' .isalnum())#True
# print('prashantjha'.isalpha())#True
# print('777'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANT'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))

# print("Prashant".find("r"))
# print("Prashant".index("r"))
# print("Prashant jha".count("a"))
#=====================================================
# for i in range(1,4):#outer loop ==> row's
#     for j in range(1,4):#inner loop ==> col's
#             print(i,end = "")
#     print()
#========================================================
# n=int(input("Enter the number of rows: ")) #5
# for i in range(1,n+1):#i=1
#     for j in range(1,n+1): #j=2
#          print(chr(64+i),end=" ")
#     print()

# n=int(input("Enter the number of rows: ")) 
# for i in range(1,n+1):#i=1
#     for j in range(1,1+i): #j=2
#          print("*",end=" ")
#     print()

# n=int(input("Enter the number of rows: ")) #5
# for i in range(1,n+1):#i=1
#     for j in range(1,n+2,-i): #j=2
#          print(chr(64+j),end=" ")
#     print()


import time
n=int(input("Enter the number of rows: ")) #5
for i in range(1,n+1):#i=1
      print(" "*(n-i),end=" ")
      for j in range(1, i+1): #j=2
           time.sleep(3)
           print("*",end=" ")
      print()