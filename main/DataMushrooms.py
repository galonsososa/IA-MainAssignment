import pandas as pd 

#This class converts the data from the .csv file into a Pandas Dataframe and adapts the data 
#to the way the algorithm reads it

#For more info about the attributes of this dataset check 'mushrooms_data/mushrooms.names' file

data = pd.read_csv('main/mushrooms_data/mushrooms.csv')

#Move the classification column to the last column position
data = data[['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 
'ring-type', 'spore-print-color', 'population', 'habitat','class']]

#Split the data in 3 sets in order to perform cross-validation
total_rows = len(data.index)

#[2708 rows x 23 columns] each subdataset
data1,data2,data3 = data[:int(total_rows/3)], data[int((total_rows/3)+1):total_rows-int(total_rows/3)+1], data[total_rows-(int(total_rows/3)):]

