# # required arguments
# def required_argu(name, year):
#     name = name
#     year = year
#     return name, year

# ra = required_argu("rrr",2022)
# print("ra",ra)




# Keyword arguments
def keyword_argu(name, year):
    name = name
    year = year
    return name, year

ka = keyword_argu(year= 2022, name="pushpa")
print("ka",ka)


# # default arguments
# def default_argu(name, year=2022):
#     name = name
#     year = year
#     return name, year

# da = default_argu('puspa')
# print("da",da)


# # variabe arguments
# def variabe_argu(*args):
#     for i in args:
#        print("i",i)
# va = variabe_argu([1,2,3])
# print("va",va)