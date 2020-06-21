import RelativeFrequency
import DataLenses
import numpy as np

#Import DataFrame from DataLenses class
df = DataLenses.df

#RelativeFrequency.eval_rel_freq(('Age','Young'), 'Hard', df)

def find_highest(D):

    #obtain all attributes except for the classification one
    attributes = list(D.columns[0:len(D.columns)-1])
    
    #obtain the name of the classification attribute
    classification_column_name = D.iloc[:,len(D.columns)-1].name
    #obtain classification values
    classifications = D[classification_column_name].unique()

    highest_rel_freq = (None,0)
    for classification in classifications:
        #print('--------------',classification,'--------------')
        for attribute in attributes:
            values = D[attribute].unique()
            for value in values:
                #calculate relative frequency of each pair (attribute,value) for each classification
                relative_frequency = RelativeFrequency.eval_rel_freq((attribute,value),classification, D)
                if (relative_frequency > highest_rel_freq[1]):
                    highest_rel_freq = (attribute,relative_frequency)
                #print(attribute,',',value,'::',relative_frequency)
    
    #the attribute with the highest relative frequency
    winner = highest_rel_freq[0]
    print('Winner is: ',winner,highest_rel_freq[1])

    return winner


def build_tree(D):
    node = find_highest(D)
    print(D[node].unique())

build_tree(df)




