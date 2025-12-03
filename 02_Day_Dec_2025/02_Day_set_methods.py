# Set in Python

# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.
# nums = { 1, 2, 3, 4}
# set2 = {1, 2, 2, 2}
# #repeated elements stored only once, so it resolved to {1, 2}
# null_set = set()
# #empty set syntax
# boolean
# int 1
# float 2.9
# str "abc"
# tuple (1,2,3)

# Note : list and dic can not stored in set because these both are mutable in nature
# list X
# dict X
# ---------

# collection = {1,2,3,4,"helo",2.4,2,5,3}
# print(collection)
# print(type(collection))
# print(len(collection))

# ------empty dectionary
# collection = {}
# print(type(collection))

# ------empty set
# collection = set()
# print(type(collection))


# Set Methods ------------------------
# set.add(el) #adds an element
# set.remove(el) #removes the elem an
# set.clear() #empties the set
# set.pop() #removes a random value

# **********Note : set is mutable but element is imutable in nature *******

# collection = set()
# collection.add(1)
# collection.add(4)
# print(collection)
# collection.remove(4)
# print(collection)
# collection.add((1,2,5))
# collection.add("Hello")
# print(collection)
# collection.add([9,5,4]) - list can Not possible to add

# print(len(collection))

# collection.clear()
# print(collection)
# print(len(collection))

# --------------

# set.union(set2) #combines both set values & returns new
# set.intersection(set2) #combines common values & returns new

set1 = {1,2,3,4,2,3,4}
set2 = {3,4,5,9,8,3}
print(set1.union(set2))
print(set1.intersection(set2))