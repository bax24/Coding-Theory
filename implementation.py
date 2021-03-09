import math
import numpy as np
def entropy(prob):
	
	entr = 0
	for i in range(len(prob)):
		#entr += prob[i]*math.log(1/prob[i], 2)
		entr += prob[i]*math.log(prob[i], 2)
	
	return -entr
	

def joint_entropy(joint_prob):
	
	joint_entr = 0
	for i in range(len(joint_prob)):
		joint_entr += joint_prob[i]*math.log(joint_prob[i], 2)
	
	return -joint_prob


def conditional_entropy(cond_prob, marg_prob):
	
	cond_entr = 0
	for i in range(cond_prob.shape[0]):
		for j in range(cond_prob.shape[1]):
			cond_entr += cond_prob[i][j]*marg_prob[i]*math.log(cond_prob[i][j], 2)
	
	return -cond_entr


def mutual_information(prob_X, prob_Y, joint_prob):
	
	prob_X = [0.603, 0.3005, 0.0965]
	prob_Y = [0.508, 0.492]
	joint_prob = np.array([[0.3115, 0.049 , 0.1475],
						   [0.2915, 0.0475, 0.153 ]])
	
	mut_inf = 0
	for i in range(len(prob_Y)):
		for j in range(len(prob_X)):
			mut_inf += joint_prob[i][j]*math.log(joint_prob[i][j]/(prob_X[j]*prob_Y[i]), 2)

	return mut_inf

prob = [3/8, 2/8, 3/8]
e = entropy(prob)
#print(e)


