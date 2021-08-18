def transpose(x):
	y = []
	if(len(x) < 1):
		return []
	for i in range(len(x[0])):
		z = []
		for j in range(len(x)):
			z.append(x[j][i])
		y.append(z)
	return y


def powers(x, a, b):
	y = []
	for i in x:
		z = []
		for j in range(a, b+1):
			z.append(i ** j)
		y.append(z)
	return y

def matmul(x1, x2):
	y = []
	for n in range(len(x1)):
		z = []
		for m in range(len(x2[0])):
			w = 0
			for k in range(len(x2)):
				w += x1[n][k] * x2[k][m]
			z.append(w)
		y.append(z)
	return y

def invert(x):
	a = x[0][0]
	b = x[0][1]
	c = x[1][0]
	d = x[1][1]
	det = a * d - c * b
	return [[d/det, -b/det], [-c/det, a/det]]

def loadtxt(p):
	f = open(p, "r")
	y = []
	for row in f.readlines():
		z = []
		for num in row.split():
			z.append(float(num))
		y.append(z)
	return y
