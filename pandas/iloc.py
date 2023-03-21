import pandas as pd
p  = pd.read_excel("C:\\Users\\SLV\\Documents\\pandas_info.xlsx")
df = pd.DataFrame(p)

###### in iloc we get the coloumns by numbers
# print(df.iloc[2,1])
# ######## coloumns with range
# print(df.iloc[0:3,0:4])
# ###### rows with row numbers * here not using range
# print(df.iloc[[2,3,6]])
#### rows and coloumns with coloumn numbers, *here not using range
# print(df.iloc[:,[2,3,5]]) # it gives all rows but 2 ,3, 5 coloumns
######## rows with row numbers and coloumsn with col numbers
print(df.iloc[[1,4],[2,3,5]])
