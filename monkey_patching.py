# changing the attributes(variables and methods) dynamically at runtime
class Test:
    def __init__(self,x):
        self.a = x
    def get_data(self):
        print("get the fetch the data from DB")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()                


t1 = Test(10)

def new_get_data(self):
    print("get the data from test db")
print("after monkey patching")
Test.get_data = new_get_data
t1.f1()
t1.f2()

        
        