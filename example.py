#Q] reverse each word in a string
#WAP a program to reverse each word in a string
#input: "Hello world"
#output: "olleH dlrow"
# s = "Hello world"
# words = s.split()
# result = ""
# for word in words:
#     result += word[::-1] + " "
# print(result.strip())


#Q] WAP to check if a string containing parantheses is valid
#test on array , list , string

#Q] apply insertion sort -> [3,5,8,6,2]
# arr = [3,5,8,6,2]
# for i in range(1,len(arr)):
#     key = arr[i]
#     j = i - 1

#     while j >= 0 and arr[j] >= key:
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j+1] = key
# print("sorted array:",arr)

#selection sort-> [20,12,10,15,2]
# arr = [20,12,10,15,2]

# for i in range(len(arr)):
#     min = i

#     j = i + 1

#     while j < len(arr):
#         if arr[j] < arr[min]:
#             min = j

#         j = j + 1   # move outside if block

#     arr[i], arr[min] = arr[min], arr[i]

# print("sorted array:", arr)
        
#Q]WA function to find all the elements that appear more than once in a list.
# sample input: [4,3,2,7,8,2,1,5,5]]
#expected output:[2,5]
# WAP to find duplicate elements in a list
# list = [4, 3, 2, 7, 8, 2, 1, 5, 5]

# duplicates = []
# visited = []

# for i in list:
#     if i not in visited:
#         visited.append(i)
#     else:
#         if i not in duplicates:
#             duplicates.append(i)
# print("Duplicate elements:", duplicates)


#Q22]WA function to sort a dictionary by keys or values in ascending or descending order
#logic:use the sorted() function with a custom key or use list comprehension
#input: {"C":3,"B":2,"A":1}
#output(Ascending by key):{"A":1,"B":2,"C":3}
#output(descending by key):{"C":3,"B":2,"A":1}
data = {"C":3,"B":2,"A":1}
# Ascending order by key
asc_dict = dict(sorted(data.items()))

# Descending order by key
desc_dict = dict(sorted(data.items(), reverse=True))

print("Ascending by key:", asc_dict)
print("Descending by key:", desc_dict)