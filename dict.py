#dictionary datatype 
mydict = {
101: "prashant",
102: "ashish",
"103" : "mohini",
"104": "trivani",
101: "ashish",
104: "ashish"
}
# print(mydict)
# #with the help of key we have to print values
# a = mydict[102]
# print(a)

#we will replace old value by new value
# mydict[102]="peter"
# print(mydict)

#only print key x=0,1
# for x in mydict:
#     print(x)

#only print values
# for x in mydict.values():
#     print(x)

#printing key and values both
# for x, y in mydict.items():
#     print(x, y)

#adding a new key:value pair
# mydict["mobile_no"]=4646463738
# print(mydict)

# mydict.pop(101)
# print(mydict)

#Quiz
# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])#

# arr = {}#{1:2,,'1':2}
# arr[1] = 1
# arr['1'] =2
# arr[1] += 1
# #print(arr)
# sum = 0 
# for k in arr:
#      sum += arr[k]
# print(sum)

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict) #{1:1}
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)
# print(my_dict)

# box = {}
# jars = {}
# crates = {}
# box['biscui'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))
#error:dictionary cannot be used as another dictionary key

# dict = {'c': 97, 'a':96, 'b':98}
# for _ in sorted(dict):
#     print (dict[_])

# rec = {"Name": "Python", "Age":"20"}
# r = rec.copy()
# print(id(r) == id(rec))
# print(id(r))
# print(id(rec))

# rec = {"Name": "Python", "Age":"20", "addr":"NJ", "Country":"USA"}
# id1 = id(rec)
# print(id1)
# del rec
# rec = {"Name": "Python", "Age":"20", "Addr": "NJ", "Country":"USA"}
# id2 = id(rec)
# print(id2)
# print(id1 == id2)

#9)Write a function to find the key with the maximum value in a dictionary
#logic: iterate through the dictionary and keep track of the key with the maximum value
# sample input: {"A":50, "B":30, "C": 70}
# Expected output: "C" 
# Function to find key with maximum value

# def max_key(d):
#     maxk = max(d, key=d.get)
#     return maxk

# d = {"A":50, "B":30, "C":70}

# print(max_key(d))

#12)write a function to find the key with the minimum value in a dictionary
#logic:iterate through the dictionary and keep track of the key with the minimum Value
#sample Input:{"X":20, "Y":10, "Z": 30}
#Expected Output:"Y"
# Function to find key with minimum value

# def min_key(d):
#     mink = min(d, key=d.get)
#     return mink

# d = {"X":20, "Y":10, "Z":30}

# print(min_key(d))

#7)write a function to count the frequency of elements in a list using a dictionary
#logic: iterate through the list and use a dictionary to store counts
#sample input:[1,2,2,3,4,3,5]
#Expected output:{"1":1, "2":2, "3":2, "4":1, "5":1}
# Function to count frequency of elements in a list

def frequency(lst):
    d = {}

    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d

l = [1,2,2,3,4,3,5]

print(frequency(l))