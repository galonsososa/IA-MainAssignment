import RelativeFrequency
import DataLenses
import DataMushrooms
import numpy as np
import pprint

#Import DataFrame from DataLenses class
df = DataLenses.df

#Three subsets for cross-validation
mushrooms_data1 = DataMushrooms.data1
mushrooms_data2 = DataMushrooms.data2
mushrooms_data3 = DataMushrooms.data3


def find_highest(D):

    #obtain all attributes except for the classification one
    attributes = list(D.columns[0:len(D.columns)-1])
    
    #obtain the name of the classification attribute
    classification_column_name = D.iloc[:,len(D.columns)-1].name
    #obtain classification values
    classifications = D[classification_column_name].unique()

    highest_rel_freq = (None,0)
    for classification in classifications:
        for attribute in attributes:
            values = D[attribute].unique()
            for value in values:
                #calculate relative frequency of each pair (attribute,value) for each classification
                relative_frequency = RelativeFrequency.eval_rel_freq((attribute,value),classification, D)
                if (relative_frequency > highest_rel_freq[1]):
                    highest_rel_freq = (attribute,relative_frequency)
    
    #the attribute with the highest relative frequency
    winner = highest_rel_freq[0]
    #print('Winner is: ',winner,highest_rel_freq[1])

    return winner


def get_subset(df, node,value):
  return df[df[node] == value].reset_index(drop=True)

#default value is an empty tree (only used the first time the function is called)
def build_tree(D, tree = None):
    node = find_highest(D) 
    #possible values for 'node'
    node_values = D[node].unique()


    #creates the tree if it is the first time the function is called (the tree is None)
    if tree is None:                    
        tree={}
        tree[node] = {}

    #check subsets where node == value (for every possible value of the node)
    for value in node_values:
        subset = get_subset(D,node,value)
        
        #clvalue = solution column value
        #counts: nº of times clvalue appears
        clValue,counts = np.unique(subset['class'],return_counts=True)
        
        if len(counts)==1:#Checking purity of subset
            tree[node][value] = clValue[0]                                                    
        else:        
            tree[node][value] = build_tree(subset) #Calling the function recursively 
                           
    return tree
    
solution_tree1 = build_tree(mushrooms_data1)
solution_tree2 = build_tree(mushrooms_data2)
solution_tree3 = build_tree(mushrooms_data3)

print('Tree 1:')
pprint.pprint(solution_tree1)
print('Tree 2:')
pprint.pprint(solution_tree2)
print('Tree 3:')
pprint.pprint(solution_tree3)



