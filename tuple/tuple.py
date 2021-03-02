#tuple, list is [], use to store multiple item in a single variable
#like an array but allow mix stuff in side, allow dupplicated memeber
fruits = ("apple", "banana", "cherry", "apple")
print(fruits)
# Have the same characteristic like lists
#can't be change
print(len(fruits))
print(fruits[0])
print(fruits[0:1])

listfruits = ["apple", "banana", "cherry"]
#can change list to tupple
tupplefruits = tuple(listfruits)
#allow mix data type
mix = (1,2,"Dog", "Orange")
print(mix)
