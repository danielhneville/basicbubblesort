import random
x = []
for i in range(100):
	x.append(int(round(random.random()*10000)))

def bubbleSort(x):
	changes = 1
	while changes>0:
		changes = 0
		for i in range(0, len(x)-1):
			one = x[i]
			two = x[i+1]
			if one > two:
				x[i], x[i+1] = x[i+1], x[i]
				changes += 1
	return x

print bubbleSort(x)