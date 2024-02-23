import random

def generate_neighbours(x):
	if x==10:
		return [9]

	if x==-10:
		return [-9]

	return [x-1,x+1]

def fx(x):
	return pow(x,3)

def hill_climb(f,initial):
	current = initial
	path = []
	while True:
		path.append(current)
		neighbors = generate_neighbours(current)
		best = max(neighbors,key=f)
		if f(best) <= f(current):
			return path, current

		current = best

def main():
	start=random.randint(-10,10)
	print("Start :",start)
	path, maxima = hill_climb(fx,start)
	# print(path)
	print("Maxima of function: ",maxima)

if __name__ == '__main__':
	main()