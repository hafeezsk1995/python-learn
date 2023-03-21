l = [0,1,2,3,4,5]
# 1
s = [i for i in l]
print("s",s)
# if condition
s1 = [i for i in l if i>2]
print("s1",s1)
# if ,else
s2 = [i if i>2 else 1 for i in l ]
print("s2",s2)

# usinf if else in if
s3 = ['no' if i==1 else 'yes' if i>1 else 'zero' for i in l]
print("f",s3)