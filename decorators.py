# def f1():
#     print("called f1")

# def f2(f):
#     f()

# f2(f1)

# # calling a function in the inside the function

# def firstfun():
#     print("started function")
#     def secondfun():
#         print("CALLed second function")

# print(firstfun())


# decarotors


def f1(fun):
    print("calling at 1")
    fun()
    # def wrapper():
    #     print("started")

    #     fun()
    #     print("endeed")
    # print("returning wrapper")    
    # return wrapper

@f1
def f():
    print("f1")


print("calling",f())