import sys
import matplotlib.pyplot as plt
from numpy import *

def powers(x, a, b):
	y = []
	for i in x:
		z = [i ** j for j in range(a, b+1)]
		y.append(z)
	return array(y)

def poly(a, x):
	# This is a pretty cool line huh?
	return sum([a[i] * (x ** i) for i in range(len(a))])

def main():
	if(len(sys.argv) != 3):
		print("wrong number of arguments! (Should be 3)")
		return

	data = transpose(loadtxt(sys.argv[1]))
	Xp = powers(data[0], 0, int(sys.argv[2]))
	Yp = powers(data[1], 1, 1)
	Xpt = transpose(Xp)

	a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
	a = a[:,0]
	X2 = linspace(data[0][0], data[0][-1], int((data[0][-1] - data[0][0]) / 0.2))
	Y2 = [poly(a, x) for x in X2]

	plt.plot(data[0], data[1], 'ro')
	plt.plot(X2, Y2)
	plt.show()

main()