import random
#function definition
def randpic(): #pic random items from list
	res = ['rock', 'paper', 'scissors']
	#choice choose random a value in list
	return random.choice(res)

def cmp(inp, randres) :	#compares string to cases and give out result
	print("Player: " + inp)
	print("Computer: " + randres)
	if inp == randres:
		print("draw")
	elif(inp == "rock" and randres == "paper"):
		print("player lose")
	elif(inp == "rock" and randres == "scissors"):
		print("player wins")
	elif(inp == "paper" and randres == "rock"):
		print("player wins")
	elif(inp == "paper" and randres == "scissors"):
		print("player lose")
	elif(inp == "scissors" and randres == "paper"):
		print("player wins")
	else:
		print("player lose")

#execution

print("Enter rock paper or scissors: ")
inp = input() #User input
cmp(inp, randpic())

