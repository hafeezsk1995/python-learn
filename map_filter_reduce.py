
# filter
lst = [1,23,4,5,6,63,34,45]

evens = list(filter(lambda n : n%2==0,lst))
print('evencs',evens,type(evens))

doubles  = list(map(lambda n : n*2, evens))
print("doubles",doubles)