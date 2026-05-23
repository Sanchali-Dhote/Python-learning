class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):#(A,D)
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False
    
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):#(A,D)
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False
    
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):#(A,D)
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False
    
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")
my_graph.add_edge("B","A")
my_graph.add_edge("B","E")
my_graph.print_graph()

#=====================================================================
class Student:
    @staticmethod #decorator
    def get_personal_detail(firstname,lastname):
        print("your personal detail=",firstname,lastname)

    @staticmethod
    def contact_detail(mobil_no, rollno):
        print("your contact detail=",mobil_no,rollno)

Student.get_personal_detail("sanchali","dhote")
Student.contact_detail(9356973907, 1001)
#destructor deallocates the resources
#garbage collection: work bydefault internally

#Single level inheritance
class College: #parent class
    def college_name(self):
        print("Modern College")

class Student(College):#child class
    def student_info(self): #member function
        print("Name: sanchali dhote")
        print("Branch: Mechanical")

obj = Student()#object create child class
obj.college_name()
obj.student_info()

#Multilevel inheritance
class College:
    def college_name(self):
        print("Modern College")

class Student(College):
    def student_info(self):
        print("Name: sanchali dhote")
        print("Branch: Mechanical")

class Exam(Student):
    def subject(self):
        print("Subject1:  Design Engineering")
        print("Subject2: Math")
        print("Subject3: C-Language")

obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()

#Multiple inheritance
class SubjMarks: # class-1
    math = int(iput("Enter paper marks of math :"))
    DE = int(input("Enter paper marks of design engineering :"))
    C = int(input("Enter paper marks of C language :"))
    english = int(input("Enter paper marks of english :"))
#=========================================================p
class PractMarks: #class-
    cpract = int(input("enter practicals marks of C language :"))
#============================================================
class Result(SubjMarks, PractMarks): #child class
    #print("if students pass in both = subject and practical paper then pass")
    def total(self):
        if self.math>=40 and self.DE>=40 and self.C>=40 and self.english>=40 and self.cpract>=20:
            print("pass")
        else:
            print("fail")
obj = Result()
obj.total()

#python only supports operator overloading
class Rbi:
    def home_loan(self):
        print("Home Loan ROI = 8%")

    def education_loan(self):
        print("Education loan =9%")

class Sbi(Rbi):
    def education_loan(self):
        print("Education loan = 10%")
        super().education_loan()

obj = Sbi()
obj.education_loan()
#====================================================================
#constructor overriding
class Rbi:
    def __init__(self):
        print("Parent class constructor")
class Sbi(Rbi):
    def __init__(self):
        print("Child class constructor")

obj = Sbi()