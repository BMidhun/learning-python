# A dictionary is a mutable, unordered, key-value paired data structure. Each key in a dictionary should be unique.

# Creating a dictionary

# 1st method 
personA_data = {"name": "Jones", "age":32, "job":"Python Developer", "company":"ABC"}

# 2nd method 

personB_data = dict(name="Jane", age=23, job="JavaScript Developer", company="ABC")

print(personA_data,personB_data)


# Access a dictionary element

my_dict = {"name":"Mohan","nationality":"India", "age":45, "job":"Civil Engineer"}


print("Name:", my_dict["name"])

print("Country:", my_dict["nationality"])

try:
  print("Lastname:", my_dict["lastname"])
except Exception as err:
  print("Error", err)


# Mutating a dictionary

my_dict["nationality"] = "USA"

print(my_dict)

# Adding new key-value pairs to an exisiting dictionary

my_dict["email"] = "mohan123@hotmail.com"

print(my_dict)


# Deleting a key value pair

# 1st method
del my_dict["nationality"]

print(my_dict)

#2nd method
email = my_dict.pop("email")

print(my_dict,email)

#3rd method
item = my_dict.popitem()

print(my_dict,item)


# Check if a key exists in the dictionary

my_dict = {"name":"Mike","country":"US", "job":"Developer"}

print("lastname" in my_dict)
print("name" in my_dict)


#Looping through the dictionary

# Loop only through the keys
dict.keys
for k in my_dict:
  print(k)  

for k in my_dict.keys():
  print(k)

# Loop only through the values
for v in my_dict.values():
  print(v)


# Loop through both key and values

for k,v in my_dict.items():
  print(k,v)


# Copying a dictionary

dictA = {"firstname":"John","lastname":"Smith","age":34,"job":"CEO of ABC"}

# Wrong method of copying a dictionary

dictB = dictA # dictB acts as reference to dictA

dictB["age"] = 45

print(dictB,dictA)

# Right methods

dictA_cpy = dictA.copy()

dictA_cpy2 = dict(dictA)

dictA_cpy["lastname"] = "Paul"

dictA_cpy2["job"] = "CEO of BDC"

print(dictA, dictA_cpy,dictA_cpy2)


# Merging a dictionary into another

dictA = {"name":"Midhun","age":25, "gender":"Male"}

dictB = {"email":"midhun123@gmail.com","phone":"97232131231231231"}

dictA.update(dictB)

print(dictA)


# What type of values can be assigned as a key in dictionary ? Any immutable object can act as a key.


dict1 = {(4,2):"point A", (3,5):"point B", (6,8):"point C"}

print(dict1)

dict2 = {True:"Roses are flowers", False:"Team India doesn't have a T20 world cup"}

print(dict2)

dict2 = {1:"Alan",2:"Ben",3:"Catherine"}

dict3 = {None:"",None:"None"}


try:
  dict3 = {{"name":"Midhun"}: {"age":34, "job":"Software Engineer"},{"name":"Melvin"}: {"age":23, "job":"Accountant"} }
except Exception as err:
  print("ERROR::",err)

try:
  dict3 = {[1,2,3]:6,[3,4,5]:12}
except Exception as err:
  print("ERROR::",err)

# Since both dictionary and list are mutable, they cannot act as a key in a dictionary