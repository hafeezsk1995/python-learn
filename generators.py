def topten():

    print("started")
    n = 1
    ls = []
    while n<=10:
        print("while loop running")
        squ = n*n
        ls.append(squ)
        n +=1
    print(ls,"ls")    
    yield ls

print("calling fror function")
val = topten()
print("calling fror loop")
for i in val:
    print("i",i)



# def topten():

#     print("started")
#     n = 1
#     while n<=10:
#         print("while loop running")
#         squ = n*n
#         yield squ
#         n +=1

# print("calling fror function")
# val = topten()
# print("calling fror loop")
# for i in val:
#     print("i",i)