# # l = ['1','3','5']

# # # converting list to tuple
# # t = tuple(l)
# # print("t",t)

# # s = ",".join(l)
# # print("s",s)

# # # convert list to dict
# # def convert(lst):
# #     dit = {}
# #     dit = {lst[i]:lst[i+1] for i in range(0,len(lst),2)}
# #     return dit
    

# # s = ['a',1,'b',2,'c',3]
# # print("convert",convert(s))    

# # lsit methods
# ls = ['1','2','3']
# # ls.append('4')
# # print("append",ls)
# # # print("append",ls.remove(4))
# # # remove
# # ls.remove('4')
# # print("ls",ls)    

# # slicing 
# print(ls[0:-1],'s')
# print(ls[-1])
# print(ls[0:])
# print(ls[0:4])
# print(ls[-1:0])
# ls.extend([1,2,3])
# print(ls)

# # pop
# print(ls.pop(1))
# print(ls)

# # insert
# ls.insert(1, "hafeez")
# print(ls)
# ls.clear()
# print(ls)    


# converting list ot str

l  = [1,'a',2,'b',3,'c']

di = {}

di = {l[i]:l[i] for i in range(len(l))}
print("di",di)

# for i in range(len(l)):
#     di.update({l[i]}=l[i+1])
        
        
        