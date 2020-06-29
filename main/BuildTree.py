import pprint

import numpy as np

import RelativeFrequency


def find_highest(D):

    #Obtain all attributes except for the classification one
    attributes = list(D.columns[0:len(D.columns)-1])
    
    #Obtain the name of the classification attribute
    classification_column_name = D.iloc[:,len(D.columns)-1].name
    #Obtain classification values
    classifications = D[classification_column_name].unique()

    highest_rel_freq = (None,0)
    for classification in classifications:
        for attribute in attributes:
            values = D[attribute].unique()
            for value in values:
                #Calculate relative frequency of each pair (attribute,value) for each classification
                relative_frequency = RelativeFrequency.eval_rel_freq((attribute,value),classification, D)
                if (relative_frequency > highest_rel_freq[1]):
                    highest_rel_freq = (attribute,relative_frequency)
    
    #The attribute with the highest relative frequency
    winner = highest_rel_freq[0]
    #print('Winner is: ',winner,highest_rel_freq[1])

    return winner


def get_subset(D, node,value):
  return D[D[node] == value].reset_index(drop=True)


def build_tree(D, tree = None):

    #Obtain the name of the classification attribute
    classification_column_name = D.iloc[:,len(D.columns)-1].name

    node = find_highest(D) 
    #Possible values for 'node'
    node_values = D[node].unique()

    if tree is None:                    
        tree={}
        tree[node] = {}

    #Check subsets where node == value (for every possible value of the node)
    for value in node_values:
        subset = get_subset(D,node,value)
        
        #clvalue = solution column value
        #counts: nº of times clvalue appears
        clValue,counts = np.unique(subset[classification_column_name],return_counts=True)
        
        #Checking purity of subset
        if len(counts)==1:
            tree[node][value] = clValue[0]                                                    
        else:        
            #Calling the function recursively
            tree[node][value] = build_tree(subset)  
                           
    return tree
