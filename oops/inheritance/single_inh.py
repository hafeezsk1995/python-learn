class Parent:
    def pdisplay(self):
        print("parent")

class Child(Parent):
    def cdisplay(self):
        print("child")

c = Child()
print(c.pdisplay())
print(c.cdisplay())