import RelativeFrequency
import DataLenses
import numpy as np
eps = np.finfo(float).eps
from numpy import log2 as log
from collections import defaultdict
import pprint

#Import DataFrame from DataLenses class
df = DataLenses.df

#RelativeFrequency.eval_rel_freq(('Age','Young'), 'Hard', df)
def find_entropy(df):
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    entropy = 0
    values = df[Class].unique()
    for value in values:
        fraction = df[Class].value_counts()[value]/len(df[Class])
        entropy += -fraction*np.log2(fraction)
    return entropy
  
  
def find_entropy_attribute(df,attribute):
  Class = df.keys()[-1]   #To make the code generic, changing target variable class name
  target_variables = df[Class].unique()  #This gives all 'Yes' and 'No'
  variables = df[attribute].unique()    #This gives different features in that attribute (like 'Hot','Cold' in Temperature)
  entropy2 = 0
  for variable in variables:
      entropy = 0
      for target_variable in target_variables:
          num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
          den = len(df[attribute][df[attribute]==variable])
          fraction = num/(den+eps)
          entropy += -fraction*log(fraction+eps)
      fraction2 = den/len(df)
      entropy2 += -fraction2*entropy
  return abs(entropy2)


def find_winner(df):
    Entropy_att = []
    IG = []
    for key in df.keys()[:-1]:
#         Entropy_att.append(find_entropy_attribute(df,key))
        IG.append(find_entropy(df)-find_entropy_attribute(df,key))
    return df.keys()[:-1][np.argmax(IG)]

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


def get_subset(df, node,value):
  return df[df[node] == value].reset_index(drop=True)

#default value is an empty tree (only used the first time the function is called)
def build_tree(D, tree = None, selected = []):
    node = find_highest(D) 
    #node = find_winner(D)
    #possible values for 'node'
    node_values = D[node].unique()

    #creates the tree if it is the first time the function is called (the tree is None)
    if tree is None:                    
        tree={}
        tree[node] = {}

    #check subsets where node == value (for every possible value of the node)
    for value in node_values:
        subset = get_subset(D,node,value)
        selected.append(node)
        #deletes from the subset all previously selected nodes, (repeted values are ignored)
        #clvalue = solution column value
        #counts: nº of times clvalue appears
        clValue,counts = np.unique(subset['lenses'],return_counts=True)            
        # print(subset)
        # print()
        # print(node,':',value,'->',clValue)
        # print()
        # print('counts',counts)
        # print('tree:')   
        # pprint.pprint(tree)
        
        if len(counts)==1:#Checking purity of subset
            tree[node][value] = clValue[0]                                                    
        # for node in list(dict.fromkeys(selected)):
        #     del subset[node]
        else:        
            tree[node][value] = build_tree(subset,selected = selected) #Calling the function recursively 
    #print(tree)               
    return tree
    

print(build_tree(df))




