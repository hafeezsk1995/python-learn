class Employee:
    global sal 
    def __init__(self,n):
        sal = n
    def salary(self):
        print(sal,'salary')
        return sal

e = Employee(10)

print(e.salary())
