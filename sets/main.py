# Sets are mutable, unordered data structures that doesn't allow duplicate values

# Creating a set

# 1st method

setA = {1,2,3,4,4,5,5,5,6}

print(setA)

# 2nd method

setB = set([1,2,3,4,4,5,5,6,6])

print(setB)

# Creating an empty set

# Wrong method

empty_set = {}

print(type(empty_set))

# Right method

empty_set = set()

print(type(empty_set))


# Mutating a set

# Adding elements to a set

my_set = {1,2,3,4,5,6}

my_set.add(6) # Trying to add duplicates

print(my_set)

my_set.add(7)

print(my_set)

# Remove elements from a set

# pop method removes the top element from set.(the method removes an element from the begining of the set and returns the removed element)

my_set.pop()

print(my_set)


# remove method. The remove method removes an element from the set and returns None, if the element is a member of the set. If not, the method raises a KeyError

try:
  my_set.remove(7)
  my_set.remove(10)
except Exception as err:
  print("ERROR:",err)

print(my_set)

# discard method. Removes the element pass to the method from the set. If the element is not a member of the set, then discard returns None

my_set.discard(5) 

my_set.discard(100)

print(my_set)


# Looping through the set

for x in my_set:
  print(x)

# Copying of a set

# wrong way

setA = {1,2}
setA_ref = setA

setA_ref.discard(2)

print(setA,setA_ref)

# Right way

setA = {1,2}

# 1st method
setA_copy = setA.copy()

#2nd method
setA_copy2 = set(setA)

# SET operations

# Union
odd_nums = set([x  for x in range(1,15,2)])
even_nums = set([x  for x in range(2,15,2)])
prime_nums = {2,3,5,7,11,13}
result = odd_nums.union(even_nums)
print(result, odd_nums)

# Intersection
result = odd_nums.intersection(prime_nums)
print(result)


# Difference 
print(odd_nums.difference(prime_nums))

# Symmetric Difference

print(odd_nums.symmetric_difference(prime_nums))

# The update method and the update version of set operations, updates the object that refers these method with the outcome of the operation. For example setA.intersection_update(setB) updates the setA with the result of intersection btw setA and setB

# Operations to check whether a set is disjoint, superset or subset to another set

# is disjoint

print(odd_nums.isdisjoint(even_nums))

# is subset 

super_set = {1,2,3,4,5,6}

sub_set = {1,2,3,4}

print(sub_set.issubset(super_set))

# os superset
print(super_set.issuperset(sub_set))


# frozenset. A frozen set is the immutable version of a set

# Creating a frozenset

fset = frozenset([1,2,3,4,4,4,5,6,7,7,7,8])

print(fset)


