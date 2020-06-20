import RelativeFrequency
import DataLenses

#Import DataFrame from DataLenses class
df = DataLenses.df

RelativeFrequency.eval_rel_freq(('Age','Young'), 'Hard', df)