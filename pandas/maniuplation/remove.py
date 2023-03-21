import pandas as pd
p  = pd.read_excel("C:\\Users\\SLV\\Documents\\pandas_info.xlsx")
df = pd.DataFrame(p)
df.drop(columns="perce") ##### this delete tempary
print(df)
###### this delete perment
df.drop(columns='perce',inplace=True)