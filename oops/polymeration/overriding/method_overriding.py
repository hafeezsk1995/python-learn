class Father:
    def transaction(self):
        print("cycle")

class Son(Father):
    def transaction(self):
        print("Bike")

s = Son()
print("s",s.transaction())        