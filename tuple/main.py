# Tuple is an immutable, iterable ordered object that allows duplicate elements

# Creating a tuple

# 1st method 

my_tupleA = ("Max",True,"Merin",False)

# 2nd method
my_tupleB = "Max",True,"Merin",False

print(my_tupleA,my_tupleB)

# 3rd method creating tuple from other iterables

my_tuple = tuple("Midhun")

print(my_tuple)

my_tuple = tuple(["Midhun","Melvin","Kevin","Jerrin"])

print(my_tuple)

# Creating a tuple containing single element.

# Wrong way

my_tuple = ("Midhun")

print(type(my_tuple)) # object of str

# Right way - If the tuple contains only single element then put a comma after the element to make the object a tuple.

my_tuple = ("Midhun",)

print(type(my_tuple)) # object of tuple


# Accessing elements in tuple

my_tuple = (12,34,56.67,True,False,"Hello", True, True,"Hello")

print("Fourth element:", my_tuple[3])

# Proving tuple is immutable 
try:
  my_tuple[3] = 2
except Exception as error:
  print("Error:",error)


# Looping through the tuple 
for x in my_tuple:
  print(x)

# Slicing of a tuple or capturing a part of the tuple
# Slicing of a tuple is similar to a list
my_tupleA = my_tuple[2:4]
print(my_tupleA)

# Length of a tuple

print("Length of my_tuple:",len(my_tuple))
  
# methods associated with a a tuple object

print(my_tuple.count(True)) # this method is also available for list as well

print(my_tuple.index("Hello")) # this method returns the index of the first occurence of the element

# making a list out of tuple and vice versa

my_list = list(my_tuple);

my_tuple = tuple(my_list)

# Spreading tuple items on assignment

college_name,*students,total = "MIT","Mark","Alan","Paul","David","Luther","Martin",6

print(college_name,students,total)


college_name,*students,total = ("MIT","Mark","Alan","Paul","David","Luther","Martin",6)

print(college_name,students,total)


# Assigning multiple values in a single 

x,y = 4,5

print(x,y)


# Note : Tuple is considered to be a more optimized data structure than a list in python. The statments below will prove it

import sys

my_list = [1,2,3,4,5,6,7,8,9,10]

my_tuple = 1,2,3,4,5,6,7,8,9,10

list_size = sys.getsizeof(my_list)

tuple_size = sys.getsizeof(my_tuple)

print(list_size,"bytes", tuple_size,"bytes")


from timeit import timeit

# Here we are using timeit module to run a set of statement using both list and tuple a 100 times to see which data structure will consume more time to complete the process.  Tuple will take less time compared to a list object

print(timeit(stmt=f'{my_list}',number=100))

print(timeit(stmt=f'{my_tuple}',number=100))
