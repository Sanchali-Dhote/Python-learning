#1. Linear Search
# time complexity O(N)
# space complexity O(1)
# if the value is never found return -1
# create  function with no parameters which are an array and a value

# def linearSearch(array, target):
#     for i in range(0, len(array)):#i=0, i=1,........i=5
#         if array[i] == target:#1 == 7, 2==7,........7==7
#             return i
#     return -1# if target value is not found

# array =[1,2,3,4,8,7,9]
# target = 6 #search the target value I.e 7
# result = linearSearch(array, target)
# if result == -1:
#     print("Target value not found")
# else:
#     print("Element found at index",result)

#removing spaces from the string
#1. rstrip()====>to remove spaces at right hand side
#2. lstrip()====>to remove spaces at left hand side
#3. strip()=====>to remove spaces both sides

# city=input("Enter your city Name:")
# scity=city.strip()
# if scity=='Hyderabad':
#     print("Hello Hyderabadi..Adab")
# elif scity=='Chennai':
#     print("Hello Madrasi...Vanakkam")
# elif scity=="Bangalore":
#     print("Hello Kannadiga...Shubhodaya")
# else:
#     print("your entered city is invalid")

#====================================================================
#Row Wise max value
# mylist =[[100, 198, 333, 323],
# [122, 232, 221, 111],
# [223, 565, 245, 764]]
# newlist=[]
# for i in range(3):#i=0
#     j=0 #
#     max = mylist[i][j]#[0][0]  |max=100
#     for j in range(4):#j=1
#         c_max = mylist[i][j]#[0][1] #c_max =198
#         if max < c_max:#100< 198
#             max = c_max
#     newlist.append(max)
# print(newlist)

#input = prashant*is*a*good*programmer
#output = ****prashantisagoodprogrammer
# name = "prashant*is*a*good*programmer"
# newname=''#prashant
# val=''#****
# for i in name:#i=8:*
#     if i !='*':
#         newname += i
#     else:
#         val+=i
# print(newname)
# print(str(val+newname))

#15/05/26
#input = aaabbbbccceeee
#output = a3b4c3e5
# name ='aaabbbbcceeeeffgg'
# newname ={}
# for i in range(len(name)):
#     key = name[i]
#     count = 0
#     for j in range(len(name)):
#         if key == name[j]:
#             count+=1
#     newname[key] = count
# #print(newname)
# for i,j in newname.items():
#     print(i,j,sep='',end='')
#=============================================================================================
# salary = int(input('Enter your salary :'))
# rating = int(input('Enter your performance appraisal rating :'))
# increment =0
# if rating >=1 and rating<=3:
#     increment = salary*10/100
# elif rating>=3.1 and rating<=4:
#     increment = salary*30/100
# elif rating>=4.1 and rating<=5:
#     increment = salary*40/100
# else:
#     print('Invalid rating')
# print('Increment Salary: ',increment+salary)
#=====================================================================================
#basicSalary = 20000
# so we have to calculate the
# HRA of basicSalary = 20%
# TA of ------------- = 30%
# DA of ------------- = 45%
#calculate GrossSalary = ?
basicSalary = 20000

# Calculate allowances
HRA = basicSalary * 20 / 100
TA = basicSalary * 30 / 100
DA = basicSalary * 45 / 100

# Calculate Gross Salary
grossSalary = basicSalary + HRA + TA + DA

# Print values
print("Basic Salary =", basicSalary)
print("HRA =", HRA)
print("TA =", TA)
print("DA =", DA)
print("Gross Salary =", grossSalary)
