# class Graph:
#     def __init__(self, vertices):
#         #Total number of vertices
#         self.V = vertices #(4)

#         #Create adjacency matrix with all 0s
#         self.matrix = [[0 for _ in range(vertices)]
#                         for _ in range(vertices)]
        
#     def add_edge(self, u,v):#(0,1)
#         self.matrix[u][v] = 1
#         self.matrix[v][u] = 1#for undirected graph

#     def remove_edge(self, u, v):
#         self.matrix[u][v] = 0
#         self.matrix[v][u] = 0
        
#     def display(self):
#         for row in self.matrix:
#             print(row)

    

# g = Graph(4)

# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,3)

# print("Adjacency Matrix")
# g.display()

#===============================================
#hashing: technique used to convert  data into a fixed size value called a hash value or hash code
#this hash value helps us store and search data very fast
#Think of hashing as: converting a big piece of information into a small addresses

# imagine we have: 10 students- easy to search,   10 lakh students - searching becomes slow
# without hashing:searching may take a lot of Time 
# with hashing: data can be found almost instantly

# befor hashing searching required
# linear search: O(n)
# binary search:O(log n)
# Hashing provides-> Average O(1) lookup Time 
# this means

# time complexity benefit
#        without hashing               with hashing
# search     O(n)                                O(1)
# insert     O(n)                                O(1)
# delete     O(n)                                O(1)

#Application                    Use of hashing

#Hash function:   hash function converts input->fixed index
#ex: hash("apple")          might produce: 23847293

#simple hash function example
#  Suppose table size = 10
# formula index=key % 10
# ex: 25%10=5
# So: 25 stored at index 5

#key 15  25  35
#  key % 10
# key         Calculation            Index 
# 15            15%10                 5
# 25            25%10                  5
# 35             35%10                 5

# Problem?  All map to same Index  this is called collision

#properties of good hash function: deterministic, fast computation , uniform distribution, hashig string
# ASCII values    C =67
#                 A = 65
#                 T = 84
# Sum: 67+65+84 = 216

#python dictionary uses: hash table
#                        open addressing
#                        dynamic resizing

#why list cannot be dictionary keys?

#why collision happens->
# infinite inputs
# limited table size

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)