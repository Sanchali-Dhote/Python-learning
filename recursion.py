#when the main problem can be divided into the similar sub problem than only we can use the recuursion
#Factorial Solution
# def factorial(num):#num=2
#     if num <= 1:#base condition
#         return 1
#     return num * factorial(num-1)
# print(factorial(4))
#==========================================================================
#capitalizeFirst Solution using recursion
# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result

#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car', 'taco', 'banana']))
#============================================================
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent-1)

# print(power(2,0))#1
# print(power(2,2))#4
# print(power(2,4))#16
#================================================================
# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])
# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))
#==================================================================
#reverse solution
# def reverse(string):#'python
#     if len(string) <= 1:#6<=1
#         return string
#     return string[len(string)-1] + reverse(string[0:len(string)-1])#n
# print(reverse('python'))#nohtyp
# print(reverse('application'))noitacilppa
#=============================================================
#recursiveRange(num):
# def recursiveRange(num):
#     if num <= 0:
#         return 0
#     return num + recursiveRange(num - 1)
# print(recursiveRange(6))#654321
#=============================================================
# def isPalindrome(string):
#     if len(string) == 0:
#         return True
#     if string[0] != string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])
# print(isPalindrome('tacocat'))
# print(isPalindrome('foobar'))
#=================================================================
#someRecursive Solution
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True

print(someRecursive([1,2,3,4], isOdd))#True
print(someRecursive([4,6,8,9], isOdd))#True
print(someRecursive([4,6,8], isOdd))#False
    
