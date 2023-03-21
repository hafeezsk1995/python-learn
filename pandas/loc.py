import pandas as pd
p = pd.read_excel("C:\\Users\\SLV\\Documents\\pandas_info.xlsx")
df = pd.DataFrame(p)

######## loc with indexing
# loc = df.loc[1]    
# print("loc",loc)

######## loc with indexing and cloumn names
# loc = df.loc[1,['name','Maths']]    
# print("loc",loc)

# ###### rows with start and stop 
# loc_start_stop = df.loc[1:5]
# print("loc_start_stop",loc_start_stop)
###### rows with start and stop 
# loc_start_stop_with_col = df.loc[1:5,['name']]
# print("loc_start_stop",loc_start_stop_with_col)
########## range to coloum names
# range_to_col = df.loc[1:5,'name':'Maths']
# print("range_to_col",range_to_col)
print(df.loc[[2,3,6]])