# class public:
#     a = 10
#     b =20
#     def pdf(self):
#         # print("pdf")
#         return "pdf"

# p = public()
# print(p.a,"variable aceesing")
# print(p.pdf(),"func aceesing")


# class protect:
#     _a = 10
#     _b =20
#     def _pdf(self):
#         # print("pdf")
#         return "pdf"

# p = protect()
# print(p._a,"variable aceesing")
# print(p._pdf(),"func aceesing")




class private:
    __a = 10
    __b =20
    def __pdf(self):
        # print("pdf")
        return "pdf"

p = private()
print(p.__a,"variable aceesing") # we cant access in private but this can happend in protected
print(p.__pdf(),"func aceesing")