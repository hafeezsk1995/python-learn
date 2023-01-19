class GrandParent:
    def gdisplay(self):
        print("grand parnet")

class Parent(GrandParent):
    def pdisplay(self):
        print("parent")

class Child(Parent):
    def cdisplay(self):
        print("child")

c = Child()
print(c.pdisplay())
print(c.cdisplay())
print(c.gdisplay())