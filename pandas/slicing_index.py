import pandas as pd
p = pd.read_excel("C:\\Users\\SLV\\Documents\\pandas_info.xlsx")
df = pd.DataFrame(p)
# print("df",df)
# # print("top 5",df.head(2),df)
####### tail
# tail_last_fie = df.tail()
# print("last_five",tail_last_fie)
### last particualr records based on givrn number
# last_particual_count  = df.tail(3)
# print("last",last_particual_count)
###### describe
# discribe = df.describe()
# print("",discribe)
# ## shape (rows, coloumns)
# shape = df.shape
# print("shape",shape)
# print("df",df)    

# start , stop , step
# slic = df[0:10:2]
# print("sli",slic)
# #### coloumn name
# colu = df['name']
# print("co",colu)

# ##### more than one colum
# more_than_col = df[['Roll_No','name']]
# print("more",more_than_col)



# ##### more than one colum with slicing
# more_than_col_slic = df[['Roll_No','name']][3:10:2]
# print("more",more_than_col_slic)
###### iter rows are return with tuple not tables format
# for iter_rows in df.iterrows():
#     print("iter_rows",iter_rows)

