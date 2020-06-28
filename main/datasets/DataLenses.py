import pandas as pd

#Input data for the dataframe
dictionary = {'Age':['Young', 'Young', 'Young', 'Young','Young','Young','Young','Young'
                ,'Pre-presbyopia','Pre-presbyopia','Pre-presbyopia','Pre-presbyopia'
                ,'Pre-presbyopia','Pre-presbyopia','Pre-presbyopia','Pre-presbyopia'
                ,'Presbyopia','Presbyopia','Presbyopia','Presbyopia','Presbyopia'
                ,'Presbyopia','Presbyopia','Presbyopia'],
        'Prescription':['Myopia','Myopia','Myopia','Myopia','Hypermetropia',
                        'Hypermetropia','Hypermetropia','Hypermetropia','Myopia',
                        'Myopia','Myopia','Myopia','Hypermetropia','Hypermetropia',
                        'Hypermetropia','Hypermetropia','Myopia','Myopia','Myopia',
                        'Myopia','Hypermetropia','Hypermetropia','Hypermetropia',
                        'Hypermetropia'],
        'Astigmatism':['-','-','+','+','-','-','+','+','-','-','+','+','-','-','+','+'
                        ,'-','-','+','+','-','-','+','+'],
        'Tear_rate':['Reduced','Normal','Reduced','Normal','Reduced','Normal',
                    'Reduced','Normal','Reduced','Normal','Reduced','Normal',
                    'Reduced','Normal','Reduced','Normal','Reduced','Normal',
                    'Reduced','Normal','Reduced','Normal','Reduced','Normal',],
        'Lenses':['None','Soft','None','Hard','None','Soft','None','Hard'
                    ,'None','Soft','None','Hard','None','Soft','None','None','None'
                    ,'None','None','Hard','None','Soft','None','None']}
 
# Create DataFrame
data = pd.DataFrame(dictionary)

#Change the dictionary into lower case
data["Age"]= data["Age"].str.lower()
data["Prescription"]= data["Prescription"].str.lower()
data["Tear_rate"]= data["Tear_rate"].str.lower()
data["Lenses"]= data["Lenses"].str.lower()
data.columns = data.columns.str.lower()