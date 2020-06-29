import pprint

import BuildTree
import CrossValidation
import datasets.DataLenses as Lenses
import datasets.DataMushrooms as Mushrooms
import RelativeFrequency

#Import DataFrame from DataMushrooms class
mushrooms_data = Mushrooms.data

#Import DataFrame from DataMushrooms class
lenses_data = Lenses.data

""" First part: Design and Implementation """

#Build tree using ID3 algorithm for Lenses data
print('Lenses data solution tree:')
pprint.pprint(BuildTree.build_tree(lenses_data))

print()

#Build tree using ID3 algorithm for Mushrooms data
print('Mushrooms data solution tree:')
#pprint.pprint(BuildTree.build_tree(mushrooms_data))

""" Second part: Experimentation """

print('Cross-validation over the Mushrooms data:')
#Perform cross-validation over the mushrooms dataset in 10 folds
CrossValidation.cross_validation(mushrooms_data)
