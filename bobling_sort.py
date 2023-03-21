
def bub(a):   
    n = len(a)-1
    print("n",n)
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]> a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a
a  = [10,3,7,4,6,1]
print(bub(a))            