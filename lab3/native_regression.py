import sys
import matplotlib.pyplot as plt
from matrix import *

def main():
	if(len(sys.argv) != 2):
		print("wrong number of arguments! (Should be 2)")
		return

	data = transpose(loadtxt(sys.argv[1]))
	Xp = powers(data[0], 0, 1)
	Yp = powers(data[1], 1, 1)
	Xpt = transpose(Xp)

	[[b], [m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))
	Y2 = [b + m * x for x in data[0]]

	plt.plot(data[0], data[1], 'ro')
	plt.plot(data[0], Y2)
	plt.show()

main()