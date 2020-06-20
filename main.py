#For the dataset i will use Pandas DataFrame library
import pandas as pd

#references
#https://www.geeksforgeeks.org/python-pandas-dataframe/#:~:text=Python%20%7C%20Pandas%20DataFrame,fashion%20in%20rows%20and%20columns.

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

#change the dictionary into lower case
df["Age"]= df["Age"].str.lower()
df["Prescription"]= df["Prescription"].str.lower()
df["Tear_rate"]= df["Tear_rate"].str.lower()
df["Lenses"]= df["Lenses"].str.lower()
df.columns = df.columns.str.lower()

# Print the output.
#print(df['age'],df.iloc[:,len(df.columns)-1])
print()


def eval_rel_freq(pair,c,D):

    attribute = pair[0].lower()
    value = pair[1].lower()
    c = c.lower()

    #obtain the name of the last column(the result? one)
    result_column_name = D.iloc[:,len(D.columns)-1].name

    #only leave the result column and the column of the pair
    D = D[[attribute,result_column_name]]

    #relative frequency = p/t
    #t: examples covered by the rule
    #p: examples correctly covered
    t = len(D[D[attribute] == value])
    p = len(D[(D[result_column_name] == c) & (D[attribute] == value)])

    result = p/t
    print('The relative frequency of the rule: [IF',attribute,'=',value,'THEN Classification =',c,'] is ',result)
    
    return result


eval_rel_freq(('Age','Young'), 'Hard', df)