dit = {'name':"hafeez","age":27}
dit.fromkeys(dit,0)
print(dit,'hjhg')

ls = [(k,v) for k,v in dit.items()]
print("ls",ls)


# # str
# s = str(dit)
# print("s",s)

# # tuple 
# tu = tuple([(k,v) for k,v in dit.items()])

# print("tu",tu)

# keys
# values
# items
# get
# update
dit.update({"school":"nagarjuna"})

print("dit",dit)
#pop
dit.pop('age')
print("di",dit)


# 
