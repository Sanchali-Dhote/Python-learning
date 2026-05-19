#in python everything is a object
# age = 33
# pi = 3.14
# name = "Sanchali"
# result = True
# print(type(age))
# print(type(pi))
# print(type(name))
# print(type(result))
#===============================================================
#why all fundamental datatypes are immutable
# math = 50
# chem = 50
# phy = 50
# print(id(math))
# print(id(chem))
# print(id(phy))
#==============================================================
#simple if
#print(2+2)
#print("2"+"2")
#a = int(input("Enter first number: "))#input function accept the value in string
#b = int(input("Enter the second number: "))
#print(a+b)
#===============================================================
#int() used to convert in integer 3.14=int= 3
# print(int(3.14))
# #print(int(10+5j))
# print(int(True))
# print(int(False))
# print(int("4.22"))
# print(int("4"))

#we cannot convert complex value to int
#we cannot convert floating point value to int 
#cant convert string name to float
#===================================================================
#complex() used to convert
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# #print(complex("name"))
# print(complex(5, -3))
# print(complex(True,False))

#bool() is used to convert
# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# #print(bool(" "))
# #print(bool("sanchali"))
#===============================================================
#simple if
# a = int(input("Enter any single digit :"))
# if a>0:
#     print("positive number")
# if a<0:
#     print("Negative number")
# if a==0:
#     print("zero")

# day = input("Enter the day name : ")
# if day == "SATURDAY" or day == "saturday" or day == "SUNDAY" or day == "sunday":
#     print("weekend")
# else:
#     print("working day")

# per = 65

# if per >= 65:
#     print("grade A")

# elif per <= 65 and per >= 50:
#     print("Grade B")

# else:
#     print("Fail")

#============================================================
# chr = ord(input("Enter any one character :"))#b
# if chr >=65 and chr<=90:
#     print("upper case")
# elif chr >97 and chr <=122:
#     print("lower case")
# elif chr >48 and chr <=57:
#     print("digit")
# else:
#     print("special symbol")
#============================================================
#membership operator
#in     #to check the values present or not
#not in #to check the values present or not
# name = "help4code"
# print('p' not in name)
#============================================================
#identity operator ->use for address comparison
#is
#not
# math = 50
# chem = 50
# print(math is chem)
#===========================================================
#if range is given then we use for loop
#for(intialization; condition; inc/dec)
#for loop incremented sequentially
# for i in range(1,11):#i=0
#     print(i*2)

# 2   3    4   5   6    7   8   9   10
#   4
#   6
#   8
#   10
#   12
#   14
#   16
#   18
#   20


#--------------------------------------
# 11  12   13  14  15   16  17.......20
# for i in range(1,11):#i=1
#     print(i*2," ",i*3," ",i*4," ",i*5)
# print("----------------------------------")
# for i in range (1, 11):#i=1
#     print(i*11," ",i*12," ",i*13," ",i*14)

#WAP to accept there paper marks and calculate total, and check if he/she si passed in all the subject so print pass else print fail
#if percentage is greater than 65 and gender = "female" so she is eligible for placement else not eligible

# phy = int(input("Enter marks of subject 1: "))
# chem = int(input("Enter marks of subject 2: "))
# math = int(input("Enter marks of subject 3: "))

# total = phy + chem + math
# percentage = total/3.0
# print("Total Marks =", total)
# print("percentage =",percentage)
# if phy >= 35 and chem >= 35 and math >= 35:
#     print("PASS")
# else:
#     print("FAIL")
# gender = input("Enter your gender M/F : ")
# if percentage >=65 and gender == "M":
#     print("Eligible for placement")
# else:
#     print("Not Eligible")
#========================================================
# for i in range (1,5):#i=1
#     if i ==3:
#         continue
#     print(i)
#==========================================================
#   1   5
#   2   4
#   4   2
#   5   1
# zip() we an take multiple  range  function inside zip()
# for i, j in zip(range(1,6), range(5,0,-1)):
#     if i ==3 and j ==3:
#         continue
#     print(i," ",j)
 #=======================================================
#13-05-2026
# num = 123 #321
# #print(5//2)
# #print(num % 10)
# a =num % 10 #a =3
# num =num // 10 #num = 12
# b = num % 10 # b = 2
# c = num // 10 #c =1
# rev = a*100 + b*10 +c*1 #300+20+1 = 321
# print(rev)


# num = 123456

# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print(rev)

Amount = int(input("Please Enter Amount for Withdraw :"))#630
print(" 100 notes= ",Amount//100)
print(" 50 notes= ",(Amount % 100)//50)
print(" 20 notes= ", ((Amount % 100) %50)//20)
print(" 10 notes= ",(((Amount % 100) %50) %20) //10)
print(" 5 notes= ",((((Amount % 100) %50) %20) %10) //5)