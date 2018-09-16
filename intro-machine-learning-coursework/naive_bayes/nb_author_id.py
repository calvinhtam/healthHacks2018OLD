#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



class classifyAndCheckAccuracy():
    def __init__(self):
        self.clf = GaussianNB()
    def fit_that_shit(self):
        t0 = time()
        self.clf.fit(features_train, labels_train)
        print "training time:", round(time() - t0, 3), "s"
        t1 = time()
        self.pred = self.clf.predict(features_test)
        print 'fitting time:', round(time() - t1, 3), 's'
        return
    def accuracy(self):
        count = 0.0
        for i in range(len(self.pred)):
            if self.pred[i] == labels_test[i]:
                count += 1
        return count/len(self.pred)
    def score(self):
        return self.clf.score(features_test, labels_test)

tester = classifyAndCheckAccuracy()
tester.fit_that_shit()
print tester.accuracy()
print tester.score()



#########################################################
### your code goes here ###




#########################################################


