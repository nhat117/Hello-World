#use case : short, filtering data
def quadratic_fx(a, b, c) :
		"""Return the function of f(x) = a x^2 + bx + c """
		return lambda x: a * x ** 2 + b * x + c
f = quadratic_fx(2, 3, - 5)
print(f(2))
#or
print(quadratic_fx(3,0,1) (2))