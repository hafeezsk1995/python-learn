class parent:
    def pdisplay(self):
        print("pdisplay")


class child1(parent):
    def c1display(self):
        print("c1display")

class child2(parent):
    def c2display(self):
        print("c2display")

c1 =child1()
print("c1",c1.c1display())

c2 =child2()
print("c2",c2.c2display())

print("c2",c2.pdisplay())