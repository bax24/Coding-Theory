import pandas as pd
import implementation as f

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
	



	
if __name__ == "__main__":
	prob = get_prob_distribution('obesity')
	print(prob)
	entr = f.entropy(prob)
	print(entr)
	