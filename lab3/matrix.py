def transpose(x):
	y = [[0] * len(x)] * len(x[0])
	i = 0
	for row in x:
		j = 0
		for elem in row:
			print("j = ", j, ", i = ", i)
			print(elem)
			y[j][i] = elem
			j += 1
			print(y)
		i += 1
	return y


def powers():
	pass

def matmul():
	pass

def invert():
	pass

def loadtxt():
	pass
