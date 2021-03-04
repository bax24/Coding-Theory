import math

def entropy(prob):
	
	entr = 0
	for i in range(len(prob)):
		entr += prob[i]*math.log(1/prob[i], 2)
	
	return entr
	
	
prob = [3/8, 2/8, 3/8]
entropy(prob)

print('coucou adri')
print('coucou Luc <3')