# i =1
# while i<=5: #i=1
#     print(i)
#     i+=1

#function- selfcontent block which execute as many as time
# def hello():# called function
#     print("hello world")

# hello()#calling function
# hello()
#difference between called function and calling function

def arithmatic(a, b):
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    sum = a+b
    sub = a-b
    div = a/b
    mul = a*b
    return sum, sub, div, mul
#print(arithmatic())
       #or
#positional argument used 
result = arithmatic(5,5)
print("Arithmatic =",result)
#it is possible to return multiple value
#()circle bracket is tuple datatype
#Que]how many types of argument we pass in function?
#Ans: 1.positional argument
#2. keyword argument
#3. variable length argument/ varialble number of arguments
#
