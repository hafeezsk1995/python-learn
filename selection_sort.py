a  = [10,3,7,4,6,1]
for i in range(len(a)):
    m_i = i
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
           m_i = j
    a[i],a[m_i] = a[m_i],a[i]        
print("a",a)            
            
        