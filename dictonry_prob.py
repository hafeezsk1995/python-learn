
# adding dict first keys and dict values in to third
dict1 = {"name_":"hafeez",'age_':27}
dict2 = {'name':"ajay",'age':37}

dict3 = dict()

dict1keys = list(dict1.keys())
dict2values = list(dict2.values())
print(dict2values)

for i in range(len(dict1keys)):
    print('v',dict2values[i])
    dict3[dict1keys[i]]  = dict2values[i]

print(dict3,"dict3")    


# sorting dictonaries with keys

# dict1 = {"name":"hafeez",'age':27}

# dictkeys = list(dict1.keys())

# dictsort = dictkeys.sort()

# new_dict = {i:dict1[i] for i in dictkeys}
# print("new_dict",new_dict)
 
