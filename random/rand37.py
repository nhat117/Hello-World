#Generate random numbers from interval[37)]
import random
def my_rand():
	#random, scale, shift, return...
	return 4 * random.random() + 3

for i in range(10) :
	print(my_rand())

print ("Uniform rand")

for i in range (10) :
	print(random.uniform(3, 7))

print("Bell curve rand mean and standard deviation")

mu = 0
sigma = 1
#normal distribution random
for i in range(20) :
	print(random.normalvariate(mu, sigma))


