# import re #
# count = 0
# pattern= re.compile("function")#string converts into bytecode
# #print(pattern)
# matcher = pattern.finditer("A function in python is defined by a def statement.python the general syntax ooks like this: def funciton-name(parameter list):statements, i.e. the function body, The parameter python list consists of  none or more parameters.") 


# for i in matcher:
#      count += 1
#      print(i.start(),"...",i.end(),"...",i.group())
#      print("The number of occurrences: ",count)
 #==============================================================
# import re
# count=0
# matcher=re.finditer("Hi","HiHiHiHi")    

# for i in matcher:
#      count+=1
#      print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences: ",count)
#================================================================
# import re
# obj = input("enter any character")#7
# objmatch= re.finditer(obj, "a7b @k9z")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())
#==================================================================
# import re
# a = input("enter string to perform match operation :")
# mtch = re.match(a, "python is very important language")
# print(mtch)
# if mtch!=None:
#     print("match found at beginning level")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("there is no matching at beginnig level")
#======================================================
#match() function
#fullmatch
# import re
# a = input("enter string to perform match operation :")
# mtch = re.match(a, "pythonisvery")
# print(mtch)
# if mtch!=None:
#     print("match found")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("full match not found")
#==============================================================
# import re
# s=input("Enter E-Mail Id")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!=None:
#     print("Valid E-Mail Id")
# else:
#     print("Invalid E-Mail id")
#================================================================
# import re
# mo = input("Enter mobile number")
# obj = re.fullmatch("[0-5]\d{9}",mo)
# if obj!=None:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")
#=============================================================
# import re
# a = input("enter string to perform match operation :")
# mtch = re.search(a, "python sss dynamic lannn")
# print(mtch)
# if mtch!=None:
#     print(mtch.start(), " ", mtch.end(), " ", mtch.group())
# else:
#     print("there is no matching anywhere ")
#=========================================================
# import re
# mtch = re.findall('[A-Z]',"abch3hdh5bk7ZQ$&*")
# print(mtch)
#=========================================================
# sub() function 
# import re
# obj = re.sub('[a-z]','*','2345 ABCD habc deff')
# print(obj)
#========================================================
# import re
# obj = re.subn('[0-7]','@','ab3gd6nkl7')
# print(obj)
# print("the string is=",obj[0])
# print("the number of replacements is=",obj[1])
#======================================================
# import re
# a= input("Enter a word to perform search operation : ")
# f1 = open("input.txt", "r")
# data = f1.read()
# mtch = re.search(a, data)
# print(mtch)
# if mtch != None:
#     print(mtch.start(), " ", mtch.end(), " ", mtch.group())
# else:
#     print("There is no matching anywhere")
#======================================================================
#Program to print the number of lines, words and characters present in the

#given file?

import os, sys

fname=input("Enter File Name: ")

if os.path.isfile(fname):

    print("File exists:", fname)

    f=open(fname, "r")

else:

    print("File does not exist:", fname)

    sys.exit(0)

lcount=wcount=ccount=0

for line in f:

    lcount=lcount+1

    ccount=ccount+len(line)

    words=line.split()

    wcount=wcount+len(words)

print("The number of Lines:", lcount)

print("The number of Words:", wcount)

print("The number of Characters:", ccount)
