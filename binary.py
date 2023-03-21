import pickle
# # l= ['vizag','anil',2]
# # a =['hyd','bhanu',3]
# # d =['kdk','anji',4]
# # e = ['vizag','anji',4]
# # f = open('binary_dat.dat',"wb")
# # pickle.dump(l, f)
# # pickle.dump(a, f)
# # pickle.dump(d, f)
# # pickle.dump(e, f)
# # f.close()

# with open('binary_dat.dat',"rb") as f:
#     count = 0 
#     while True:
#         try:
#             row = pickle.load(f)
#             # print all data
#             #print('row',row)
#             # print only first value
#             #print('row',row[0])
#             # if row[0].lower() == 'vizag':
#             #    print('row',row)
#             summ = 0
#             # if row[0].lower() == 'vizag':
#             #    print('row',row)
#             #    summ = summ + row[2]
#             #    print("sum",summ)
#             if row[0].lower() == 'vizag':
#                count += count
               
               
            
#         except EOFError:
#             break    
        
#         # print("sumsdv",summ)   
#     print("count",count)   
    

# one file have event , sportsname  and city name in list format but take event and sportsname and store in another f
# file in dictonary format

f = open('binary_dat.dat',"wb")
a  = ['venet','crivkey','ongole']
b = ['farwell','baseball','kdkr']
c = ['rally','ockey','cithu']

pickle.dump(a, f)    
pickle.dump(b, f)   
pickle.dump(c, f)   
f.close()

f = open('binary_dat.dat','rb')
f1 = open('binary_dat1.dat','wb')
while True:
    try:
        row  = pickle.load(f)
        dt = {row[0]:row[1]}
        print("dt",dt)
        pickle.dump(dt, f1)
    except EOFError:
        break
f1 = open('binary_dat1.dat','rb')    
row  = pickle.load(f1)
print("rows",row)
f.close()
f1.close()
            
        
        
        
        
