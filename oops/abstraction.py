from abc import ABC, abstractmethod

class Abstactdemo(ABC):
    @abstractmethod
    def display(self):
        None

class Demo(Abstactdemo):
    def display1(self): # here method name should be same as above
        print('display prints')

# obj = Abstactdemo()
# print("obj",obj.display())

d = Demo()

print("demo",d.display1())