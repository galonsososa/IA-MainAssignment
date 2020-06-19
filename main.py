#For the dataset i will use Pandas DataFrame library
import pandas as pd

#Input data for the dataframe
data = {'Age':['Young', 'Young', 'Young', 'Young','Young','Young','Young','Young'
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
df = pd.DataFrame(data)
# Print the output.
print(df)