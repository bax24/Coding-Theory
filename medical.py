import pandas as pd
import implementation as f
import numpy as np

df = pd.read_csv (r'P1_medicalDB.csv')

def get_prob_distribution(variable):
	
	prob = []
	N = df.shape[0]
	card = len(df[variable].value_counts())
	
	for i in range(card):
		p = df[variable].value_counts()[i]/N
		prob.append(p)
	
	return prob
	

def get_cardinality(variable):
	return len(df[variable].value_counts())
	
# à tester avec 2 autres variables
def get_cond_prob(variable, given, disp = False):
	
	card_variable = len(df[variable].value_counts())
	card_given = len(df[given].value_counts())
	prob = np.zeros((card_given , card_variable))
	
	for i in range(card_given):
		N = df[given].value_counts()[i]
		for j in range(card_variable):
			name_var = df[given].value_counts().index.tolist()[i]
			if disp:
				print(name_var)
			prob[i][j] = df[df[given] == name_var][variable].value_counts(sort = False)[j]/N

	df[variable].value_counts(sort = False)

	return prob

def get_joint_prob(variable_1, variable_2):
	
	card_variable_1 = len(df[variable_1].value_counts())
	card_variable_2 = len(df[variable_2].value_counts())
	joint_prob = np.zeros((card_variable_2 , card_variable_1))
	
	cond_prob = get_cond_prob(variable_1, variable_2)
	marg_prob = get_prob_distribution(variable_2)
	
	for i in range(cond_prob.shape[0]):
		for j in range(cond_prob.shape[1]):
			joint_prob[i][j] =  cond_prob[i][j]*marg_prob[i]
	
	return joint_prob
	
if __name__ == "__main__":	
	
	
	variable = 'DIS'
	given = '
	p = get_cond_prob('DIS', 'sex', True)
	
	
	# Entropy of each variable
	card = []
	entropies = []
	
	for variable in list(df.columns):
		card.append(get_cardinality(variable))
		prob_dist = get_prob_distribution(variable)
		entropy = f.entropy(prob_dist)
		entropies.append(round(entropy, 3))
		
	print(card)	
	print(entropies)
	
	# Conditional entropy of the disease given each variables	
	
	cond_entropies = []
	variable = 'DIS'
	
	for given in list(df.columns):
		if given == variable:
			continue
		cond_prob = get_cond_prob(variable, given)
		marg_prob = get_prob_distribution(given)
		cond_entr = f.conditional_entropy(cond_prob, marg_prob)
		cond_entropies.append(round(cond_entr, 3))
		
	
	print(cond_entropies)
	
	# Mutual information
	
	variable_1 = 'obesity'
	variable_2 = 'age'
	
	joint_prob = get_joint_prob(variable_1, variable_2)
	prob_var_1 = get_prob_distribution(variable_1)
	prob_var_2 = get_prob_distribution(variable_2)
	mut_inf = f.mutual_information(prob_var_1, prob_var_2, joint_prob)
	
	cond_prob = get_cond_prob('obesity', 'age')
	marg_prob = get_prob_distribution('age')
	cond_entr = f.conditional_entropy(cond_prob, marg_prob)
	
	
	
	p = get_prob_distribution('obesity')
	entr = f.entropy(p)
	
	
	
	
	