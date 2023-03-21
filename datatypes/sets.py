st = {1,2,43,3,4,
      }
print()

# convert to list
l = list(st)
print("l",l)

# convert to dict
dit = dict.fromkeys(st,0)
print("di",dit)

# methods
st.add(9)
print("st",st)
st.remove(43)
print("st",st)
st.pop()
print(st,"st")
# update
# st.update({0,0,0,1,1,2,3})
x = {0,0,0,1,1,2,3}
# print(dit)
# intersectipm\
st.intersection(x)
print(st,"st")    