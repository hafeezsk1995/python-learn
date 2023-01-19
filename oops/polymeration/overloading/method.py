class MethodOverload:
    def display(self, a=None,b=None):
        print(a,b)

mv = MethodOverload()
print("mv",mv.display())
print("mv1",mv.display(10))
print("mv1",mv.display(10,90))