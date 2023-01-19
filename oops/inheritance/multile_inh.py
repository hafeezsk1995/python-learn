class Father:
    def fdisplay(self):
        print("fdisplay")

class mother:
    def mdisplay(self):
        print("mdisplay")

class child(Father,mother):
    def cdisplay(self):
        print("cdisplay")


c =child()
print(c.cdisplay())
print(c.mdisplay())
print(c.fdisplay())

