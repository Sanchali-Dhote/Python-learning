# import logging
# logging:basicConfig(filename="newfile.txt", level=logging.DEBUG)
# try:
#     a=int(input("enter first integer no"))
#     b=int(input("enter second integer no"))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("Logging Level is set up. Check 'newfile.txt' for details.")
#why use file handling ?

import csv
f = open("employee.csv",'a')
a = csv.writer(f)
# a.writerow(["EmpID","Emp Name","Emp Age"])
empid =int(input("Enter you EMpid :"))
empName = input("Enter employee name :")
age = int(input("Enter employee age :"))
a.writerow([empid,empName,age])
print("file has created")