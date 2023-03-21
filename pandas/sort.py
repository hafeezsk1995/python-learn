import pandas as pd
p  = pd.read_excel("C:\\Users\\SLV\\Documents\\pandas_info.xlsx")
df = pd.DataFrame(p)
###### sort by asc
# print(df.sort_values("Maths"))
###### sort by desc
# print(df.sort_values("Maths",ascending=False))
##### sort with twpo coloumsn
print(df.sort_values(["Maths","Social"]))

