#types of variable(instance var)
# class New:
#       def __init__(self):
#            self.a = 10
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# Obj1.a = 20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

#static variable ->using the class name we can modify ,delete, static variable
# class New:
#       a=10
      
#       def __init__(self):
#             self.name="sanchali"
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# New.a=50
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

#for every object a separate copy of instance variable created but in case of static 
#variable only one copy will be created and it is accessble for every object of the class
class College:
    collegename= "Modern College" #static variable (1 memory)
    def __init__(self):
        self.studentname = "sanchali" #

principal = College()
teacher  = College()
accountant = College()
print("principal=",principal.collegename,"....",principal.studentname)
print("teacher =",teacher.collegename,"....",teacher.studentname)
print("accountant=",accountant.collegename,"....", accountant.studentname)
College.collegename="HBD"
principal.studentname="sanchali dhote"
print("principal=",principal.collegename,"|",principal.studentname)
print("teacher =",teacher.collegename,"|",teacher.studentname)
print("accountant=",accountant.collegename,"|",accountant.studentname)