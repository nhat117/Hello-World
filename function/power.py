def power(base, root):
	#base case
	if root == 0:
		return 1
	return base * power(base, root -1)
#main function
print("Enter base : ")
base = input()
print("enter root:")
root = input()
txt = "{} root {} is"
print(txt.format(base, root), pow(int(base),int(root)))
