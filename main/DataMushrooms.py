import pandas as pd 

data = pd.read_csv('main/mushrooms.csv')

#print('before',list(data.columns))

#print(list(data.iloc[:,1:len(data.columns)].columns))

#columns_without_classification = list(data.iloc[:,1:len(data.columns)].columns)

#print(columns_without_classification)

data = data[['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 
'ring-type', 'spore-print-color', 'population', 'habitat','class']]

#print('after',list(data.columns))