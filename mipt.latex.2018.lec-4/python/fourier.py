import numpy as np 

XMAX = 2
N = 1000

x = np.arange(-XMAX, XMAX, 2*XMAX/N)
y = np.zeros(N)
for k in range(5):
    y += 2 * (-1)**k * np.sin(np.pi*(k+1)*x) / (k+1) / np.pi
    
f = open("../data/fourier.dat", "w")
f.write("x\tS_k")

for i in range(len(x)):
	f.write("\n{}\t{}".format(x[i], y[i]))