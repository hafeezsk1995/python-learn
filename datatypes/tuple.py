tu =(('1',2),('3',3),('4',4))
ts = (1,2)

# convert tuple to list
# ls = list(tu)
# print(ls)

# s = "".join(tu)
# print("s",s)

# tuple 
dic = dict((k,v) for k,v in tu)
print("dics",dic)

# tuple methods
print(ts.count(2))
print("index",ts.index(1))