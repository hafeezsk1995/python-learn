# numb = [1,2,2,34,12,2]
# numb1 = numb

# numb1[1] = 0

# print("num",numb)
# print("num1",numb1)


import copy
# * in shallow copy it doesnt change the object of the old list ex : new_list[0] = ['a','b','c'] but it chages iteams
# shallow copy
# old_list = [[1,2,3],[23,3,44]]
# new_list = copy.copy(old_list)
# #new_list[0] = ['a','b','c'] 
# new_list[0][0] = 'a'
# print("old list",old_list)
# print("new list",new_list)


# deep copy

old_list = [[1,2,3],[23,3,44]]
new_list = copy.deepcopy(old_list)
new_list[0] = ['a','b','c']  
#new_list[0][0] = 'a'
print("old list",old_list)
print("new list",new_list)



