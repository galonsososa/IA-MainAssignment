import pandas as pd

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