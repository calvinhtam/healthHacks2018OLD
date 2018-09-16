#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
maxBonus = 0
bigDaddy = ''
secondMaxBonus = 0
bigBoi = ''
for k, v in data_dict.items():
    if v['bonus'] != 'NaN':
        if v['bonus'] > maxBonus:
            if secondMaxBonus < maxBonus:
                bigBoi = bigDaddy
                secondMaxBonus = maxBonus
            maxBonus = v['bonus']
            bigDaddy = k
        elif v['bonus'] > secondMaxBonus:
            secondMaxBonus = v['bonus']
            bigBoi = k
print(bigDaddy, bigBoi)

data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
### your code below



