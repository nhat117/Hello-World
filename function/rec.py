def factorial(inval):
	#base case
	if inval == 1:
		return inval
	return inval * factorial(inval -1)
#main function
print("Enter num : ")
inval = input()
inval = int(inval)
txt = "factorial of {} is"
print(txt.format(inval), factorial(inval))
