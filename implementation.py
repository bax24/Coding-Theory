import math

def entropy(prob):
	
	entr = 0
	for i in range(len(prob)):
		#entr += prob[i]*math.log(1/prob[i], 2)
		entr += prob[i]*math.log(prob[i])
	
	return -entr
	

def joint_entropy(joint_prob):
	
	joint_entr = 0
	for i in range(len(joint_prob)):
		joint_entr += joint_prob[i]*math.log(joint_prob[i])
	
	return -joint_prob


def conditional_entropy(cond_prob, marg_prob):
	
	cond_entr = 0
	for i in range(len(cond_prob)):
		cond_entr += cond_prob[i]*marg_prob[i]*math.log(cond_prob[i])
	
	return -cond_entr


def mutual_information(prob_X, prob_Y, joint_prob):
	
	mut_inf = 0
	for i in range(len(prob_X)):
		for j in range(len(prob_Y)):
			mut_inf += joint_prob[i+j]*math.log(joint_prob[i+j]/(prob_X[i]*prob_Y[j]))

	return mut_inf

prob = [3/8, 2/8, 3/8]
e = entropy(prob)
print(e)


