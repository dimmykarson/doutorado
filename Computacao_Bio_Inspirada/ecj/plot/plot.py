import matplotlib.pyplot as plt
import os
import sys


file_name = sys.argv[1]

data = open(file_name)

fit = []

for line in data:
	line = line.replace('\n', '')
	aux = line.split(' ')
	if aux[0] == 'Fitness:':
		fit.append(-float(aux[1]))

plt.plot(fit)
plt.yscale('log')
plt.show()