import pprint

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

import BuildTree
import datasets.DataMushrooms


def cross_validation(D):
    #Split the model in k = 10 pieces
    kf = KFold(n_splits=10)

    #Create an empty list with accuracy values
    scores = []

    #Initialize a counter to check which value of 'k' is being executed
    k = 0

    #kf.split splits using k-fold cross-validation in 10 pieces mushrooms_data, separating test_data from train_data
    for train_index, test_index in kf.split(D):
        k = k + 1
        print('K:',k,'----------------------------------------------------------------')
        #print('TRAIN:',train_index,'TEST:',test_index) #uncomment this line in case if wanting to check which indexes are 
        #being used for training and for testing
        #Store in 'tree' the algorithm solution for the training_data
        tree = BuildTree.build_tree(D.iloc[train_index,:])
        pprint.pprint(tree)
        test(D.iloc[test_index,:],tree,scores)
   
    average = sum(scores) / len(scores)
    print('--------------------------------------------------')
    best = best_result(scores)
    print('The average accuracy is',average)
    print('The best result is',best)



#Takes the test_data features_columns of a row and follows the trained tree to guess the solution
def predict(query,tree,default = 1):

    for key in list(query.keys()):
        if key in list(tree.keys()):
            try:
                result = tree[key][query[key]] 
            except:
                #If not found return '1', which acts as false later in the comparison
                return default
  
            result = tree[key][query[key]]
            if isinstance(result,dict):
                return predict(query,result)
            else:
                return result

#Compare the inputed data (test_data) with the predictions made from the trained tree
def test(data,tree,scores):
    #Create a new dictionary with feature columns (all columns except the classification one)
    features = data.iloc[:,:-1].to_dict(orient = "records")

    #Obtain the name of the classification attribute
    classification_column_name = data.iloc[:,len(data.columns)-1].name
    
    #Create a empty DataFrame in whose columns the prediction of the tree are stored
    predicted = pd.DataFrame(columns=["predicted"])

    #Calculate the prediction accuracy
    for i in range(len(data)):
        #Store the prediction value
        predicted.loc[i,"predicted"] = predict(features[i],tree,1.0) 
    #print(data["class"]) #uncomment this line in case of wanting to check the test data
    #print(predicted["predicted"]) #uncomment this line in case of wanting to check the predictions is making

    #If the prediction_value == test_data_value add 1. After it calculate percentage in respect to the total values
    accuracy = (np.sum(predicted["predicted"].values == data[classification_column_name].values)/len(data))*100
    scores.append(accuracy)
    print('The prediction accuracy is: ',accuracy,'%')

def best_result(scores):
    k = 0
    best = 0
    for score in scores:
        k = k + 1
        print('k:',k,'has an accuracy of',score)
        if score > best:
            best = score
    return best
