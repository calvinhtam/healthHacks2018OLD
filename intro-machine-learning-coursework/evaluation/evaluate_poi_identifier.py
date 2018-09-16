#!/usr/bin/python 


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

sort_keys = '../tools/python2_lesson13_keys.pkl'
data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, random_state= 42, test_size=0.30)
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print(clf.score(features_test, labels_test))
count = 0
for i in labels_test:
    if i:
        count += 1
print(count, len(labels_test))
metric_data = metrics
print(metric_data.precision_score(labels_test, clf.predict(features_test)))
print(metric_data.recall_score(labels_test, clf.predict(features_test)))

### your code goes here 


