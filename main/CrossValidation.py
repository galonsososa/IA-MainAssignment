import numpy as np
import pandas as pd
import DataMushrooms
import main
from sklearn.model_selection import KFold
import pprint

#Split the model in k = 10 pieces
kf = KFold(n_splits=10)

#Import mushrooms data
mushrooms_data = DataMushrooms.data

#Create an empty list with accuracy values
scores = []
#Create a variable for the best result
best_result = 0

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
def test(data,tree):
    global best_result
    #Create a new dictionary with feature columns (all columns except the classification one)
    features = data.iloc[:,:-1].to_dict(orient = "records")
    
    #Create a empty DataFrame in whose columns the prediction of the tree are stored
    predicted = pd.DataFrame(columns=["predicted"])

    #Calculate the prediction accuracy
    for i in range(len(data)):
        #Store the prediction value
        predicted.loc[i,"predicted"] = predict(features[i],tree,1.0) 
    #print(data["class"]) #uncomment this line in case of wanting to check the test data
    #print(predicted["predicted"]) #uncomment this line in case of wanting to check the predictions is making

    #If the prediction_value == test_data_value add 1. After it calculate percentage in respect to the total values
    accuracy = (np.sum(predicted["predicted"].values == data["class"].values)/len(data))*100
    scores.append(accuracy)
    if (accuracy > best_result):
        best_result = accuracy
    print('The prediction accuracy is: ',accuracy,'%')
  


def cross_validation():
    #Initialize a counter to check which value of 'k' is being executed
    k = 0
    #kf.split splits using k-fold cross-validation in 10 pieces mushrooms_data, separating test_data from train_data
    for train_index, test_index in kf.split(mushrooms_data):
        k = k + 1
        print('K:',k,'----------------------------------------------------------------')
        #print('TRAIN:',train_index,'TEST:',test_index) #uncomment this line in case if wanting to check which indexes are 
        #being used for training and for testing
        #Store in 'tree' the algorithm solution for the training_data
        tree = main.build_tree(mushrooms_data.iloc[train_index,:])
        pprint.pprint(tree)
        test(mushrooms_data.iloc[test_index,:],tree)
   
average = sum(scores) / len(scores)
print('The average accuracy is',average)
print('The best result is',best_result)
