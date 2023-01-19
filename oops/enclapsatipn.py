# class Encap:
#     a= 10
#     def display(self):
#         print('welcome')


# e = Encap()
# print("e",e.display())


# Private
class Encap_private:
    _a= 10
    def display(self):
        print('welcome')
        print(self._a)


e = Encap_private()
print("e",e._a)