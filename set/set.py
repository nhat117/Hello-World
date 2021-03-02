#set like lists but end in {} bracket
fruits = {"apple", "banana", "cherry"}
#use if to check if a members is in set
if "apple" in fruits :
	print("Yes")
#use add to add orange in set
fruits.add("orange")
print(fruits)
#can add multiple item in to set
more_fruits = ["mango", "grapes", "strawberry"]
fruits.update(more_fruits)
#remove memebrs
#fruits.remove("oranfe")
fruits.discard("orange")
print(fruits)

