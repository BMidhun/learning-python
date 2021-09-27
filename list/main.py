# Creating list in Python

# 1st method

listA = [1,2,3,4,5]

listB = list()

print(listA, listB)

# The list in Python is a ordered, mutable and structure that hold multiple types of values. Also we can add duplicate values inside of a list. Each list item is being referred using its index. The list index starts from 0.

# Accessing a list item

print("The second item of the list is::", listA[1])

# listA[100]  This is an error since the length of listA is 5 and the developer is trying to access the 100th element which doesn't FileExistsError

# Negative indexing - We can use negative integers as index to access an list element in the list. -1 represents the last element, -2 represent the second last element and so on.

print("The 2nd last item of the list is::",listA[-2])


# Print every element in the list

for element in listA:
  print(element)

# Checking whether an element exists in a list

# 1st method
cart = ["apple","milk","butter","bread"]

print("Is cheese added to the cart::", ("cheese" in cart))

#2nd method - this throws a ValueError saying cheese is not in list
# cart.index("cheese")


# Length of a list

print("Number of items in the cart::",len(cart))


# Update and delete operation in list

# Updating a list

# Adding elements to the end of the list
cart.append("lettuce") 
print("The updated cart is::", cart)

# Inserting element to a specific index

cart.insert(2,"cheese")

print("The updated cart is::", cart)

# Delete elements from the list

# Removing the last element from the list.
cart.pop()

print("The updated cart is::", cart)

# Removing an element using its index

cart.pop(2)

print("The updated cart is::", cart)

# Remove an element using its value. The remove only removes the first occurrence of a value 
cart.remove("apple")

print("The updated cart is::", cart)


# Creating copy of a list

# Wrong method. Here the developer is trying create a reference tmp for listC, so changes made to tmp affects listC and vice versa.

listC = [100, True, "Mango"]
tmp = listC

tmp.remove("Mango")

print("listC:",listC,"Temp:",tmp)

# Right methods of creating a copy of list :

mlist = ["Trump","Vince","Obama","Charlie","Kate"]

mlist_cpyA = mlist.copy() # 1st method

mlist_cpyB = list(mlist) # 2nd method

mlist_cpyC = mlist[:] #3rd method

print(mlist_cpyC)

mlist_cpyA.pop()

mlist_cpyB.pop(2)

mlist_cpyC.append("John")

print("MLIST:",mlist, "MLIST COPYA:", mlist_cpyA, "MLIST COPYB:",mlist_cpyB,
 "MLIST COPYC:",mlist_cpyC)


# Sorting list


# The sort method of a list object sorts the object itself and returns None. 

# The built-in sorted method returns a sorted copy of the list and the original list will not be changed 

my_list = ["Midhun","Alan","David"]

my_list_sorted_cpy = sorted(my_list)

print(my_list, my_list_sorted_cpy)

my_list.sort()

print(my_list)



# Creating a list of elements having same value

same_value_list = ["Midhun"] * 5

print(same_value_list)


# List extension or adding to list

wishlistA = ["Laptop","Camera","Pendrive","GoPro"]

wishlistB = ["Laptop","Protein Powder","Dumbells","Skipping Rope"]

cart = wishlistA + wishlistB

print("Cart:", cart)

cart = ["TV","Washing Machine"]

cart.extend(wishlistA) # equivalent to cart = cart + wishlistA

print(cart)


# Capturing a part of the list 

cart = ["Laptop","Protein Powder","Dumbells","Skipping Rope","TV","Washing Machine","Kettle","Knives","Oven","Fridge","Stablizer"]

# cart[start:end:step]

print(cart[3:5])

print(cart[3:7:2])

print(cart[:8])

print(cart[5:])

# Reverse a list in a single step

print("reverse of cart::", cart[::-1])

print(cart[-1:])

print(cart[:-1])


# List Generation 

squared_list = [x**2 for x in range(0,10)]

print("Squared list:",squared_list)