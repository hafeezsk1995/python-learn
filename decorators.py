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


# # decarotors


# def f1(fun):
#     print("calling at 1")
#     fun()
#     # def wrapper():
#     #     print("started")

#     #     fun()
#     #     print("endeed")
#     # print("returning wrapper")    
#     # return wrapper

# @f1
# def f():
#     print("f1")


# print("calling",f())


#  decarotors with  out arguments and with argumrnts

# def decar_fun(orginal_func):
#     def wraper():
#         print("calling a function before orginalk" )
#         d = orginal_func()
        
#         print("calling a function after orginalk" )
#     return wraper    

# @decar_fun
# def diaplay():
#     print("calling diaplay")
# print("d",diaplay())    

def decar_fun(orginal_func):
    def wraper(a,b):
        print("calling a function before orginalk" )
        d = orginal_func(a,b)
        print("a,b",a+b)
        
        print("calling a function after orginalk" )
    return wraper    

@decar_fun
def diaplay(a,b):
    print("calling diaplay")
    return 'd'
print("d",diaplay(10,20))    