import pandas as pd
import implementation as f
import numpy as np

df = pd.read_csv (r'P1_medicalDB.csv')

def get_prob_distribution(variable):
	
	prob = []
	N = df.shape[0]
	card = len(df[variable].value_counts())
	print(df[variable].value_counts())
	
	for i in range(card):
		p = df[variable].value_counts()[i]/N
		prob.append(p)
	
	return prob
	

# à tester avec 2 autres variables
def get_cond_prob(variable, given):
	
	card_variable = len(df[variable].value_counts())
	card_given = len(df[given].value_counts())
	prob = np.zeros((card_given , card_variable))
	
	
	for i in range(card_given):
		for j in range(card_variable):
			prob[i][j] = 	df[df[given] == df[given].value_counts().index.tolist()[i]][variable].value_counts()[j]

	
if __name__ == "__main__":
	prob = get_prob_distribution('obesity')
	print(prob)
	entr = f.entropy(prob)
	print(entr)
	