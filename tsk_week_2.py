# STRINGS
# Concatenation
"""age = "high"
txt = "My name is John, I am " + age
print(txt)

age = 36
txt = "My name is John, and I am {}" #curly braces
print (txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

viking = "We are the so-called Vikings from the north."
print (viking)

"""

# BOOLEANS
# Booleans represent one of two values: True or False.
# https://www.w3schools.com/python/python_booleans.asp 

"""
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = "200"
b = "33"

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


def myFunction():
    return True

myFunction() #this will execute the print command inside of your function
"""

# OPERATORS
# We'll get back to Bitwise operators later.

# ARRAYS: lists, tuples, Sets and Dictionaries
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-1:-4])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = ["apple", "banana", "cherry"]
del thislist
print (thislist)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)

thisset = {"apple", "banana", "cherry"}

thisset.update(["apple", "mango", "grapes"])

print(thisset)


# LOOPS

a = 3
b = 4

if a<b:
  print ("A is less than B")

i = 1
while i < 6:
  i += 1
  if i == 3:
    print ("Woohoo, we get to continue!")
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  '''
for x in [0, 1, 2]:
  