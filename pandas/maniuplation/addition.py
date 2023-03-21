######### adding default
import pandas as pd
p  = pd.read_excel("C:\\Users\\SLV\\Documents\\pandas_info.xlsx")
df = pd.DataFrame(p)
# df["total"] = 0
# print("df",df)
######### adding by expersion
# df["total"] = df["Maths"] + df["Social"]
df["perce"] = "pass/fail"
print("df",df)
