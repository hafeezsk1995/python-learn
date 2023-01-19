# find out how many times repeated count

# def repeated_count(names):
#     names_count = {}
#     for name in names:
#         if name in names_count:

#             names_count[name] +=1
#         else:
#             names_count[name] = 1
#     return names_count        
# names = ['hafeez','hafeez','nani']
# r_c = repeated_count(names)
# print("rc",r_c)

def odd_even_number(number):
    if number%2 == 0:
        return f"even number is {number}"
    else:
        return f"odd number is {number}"

print(odd_even_number(11))