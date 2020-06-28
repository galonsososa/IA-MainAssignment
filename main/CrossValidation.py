import numpy as np
import pandas as pd
import DataMushrooms
import main
from sklearn.model_selection import KFold
import pprint

#Split the model k = 10 pieces
kf = KFold(n_splits=10)

#Import mushrooms data
mushrooms_data = DataMushrooms.data

#Initialize scores empty list
scores = []

#Feature columns
X = mushrooms_data.iloc[:, 0 : 22]
#Output column
y = mushrooms_data.iloc[:, 22]

i = 0


"""     #print("TRAIN:", train_index, "TEST:", test_index)
    #print(mushrooms_data.iloc[train_index,:])
    #X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    #y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    model_test = main.build_tree(mushrooms_data.iloc[test_index,:])
    model_train = main.build_tree(mushrooms_data.iloc[train_index,:])
    print('Model train:')
    pprint.pprint(model_train)
    print('Model test:')
    pprint.pprint(model_test) """

def predict(query,tree,default = 1):
    
    #1.
    for key in list(query.keys()):
        if key in list(tree.keys()):
            #2.
            try:
                result = tree[key][query[key]] 
            except:
                return default
  
            #3.
            result = tree[key][query[key]]
            #4.
            if isinstance(result,dict):
                return predict(query,result)

            else:
                return result

        
"""    
def train_test_split(dataset):
    training_data = dataset.iloc[:80].reset_index(drop=True)#We drop the index respectively relabel the index
    #starting form 0, because we do not want to run into errors regarding the row labels / indexes
    testing_data = dataset.iloc[80:].reset_index(drop=True)
    return training_data,testing_data

training_data = train_test_split(dataset)[0]
testing_data = train_test_split(dataset)[1]  """



def test(data,tree):
    #Create new query instances by simply removing the target feature column from the original dataset and 
    #convert it to a dictionary
    queries = data.iloc[:,:-1].to_dict(orient = "records")
    
    #Create a empty DataFrame in whose columns the prediction of the tree are stored
    predicted = pd.DataFrame(columns=["predicted"])
    #pd.DataFrame(pd.np.empty((0, len(data)))) 
    #setNames(data.frame(matrix(ncol = 3, nrow = 0)), c("name", "age", "gender"))
    #predicted.reindex([range(len(data))])

    #print(predicted["predicted"])

    
    #Calculate the prediction accuracy
    for i in range(len(data)):
        #data.index.values
        #predicted.set_axis([data.index.values], axis='index', inplace=False)
        #print(i)
        predicted.loc[i,"predicted"] = predict(queries[i],tree,1.0) 
    print(data["class"])
    print(predicted["predicted"])
    print('The prediction accuracy is: ',(np.sum(predicted["predicted"].values == data["class"].values)/len(data))*100,'%')
  

    """
Train the tree, Print the tree and predict the accuracy
"""

for train_index, test_index in kf.split(mushrooms_data):
    i = i + 1
    print('K:',i,'----------------------------------------------------------------')
    print('TRAIN:',train_index,'TEST:',test_index)
    tree = main.build_tree(mushrooms_data.iloc[train_index,:])
    pprint.pprint(tree)
    test(mushrooms_data.iloc[test_index,:],tree)