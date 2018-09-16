#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print (len(enron_data['SKILLING JEFFREY K']))
print(sum(1 if enron_data[k]['poi'] else 0 for k in enron_data))
print(sum(1 if enron_data[k]['email_address'] != 'NaN' else 1 for k in enron_data))
print(sum(1 if enron_data[k]['total_payments'] == 'NaN' else 0 for k in enron_data))
#for k in enron_data:
#if enron_data[k]['poi'] == 1:
#print('ji')
from feature_format import *

feature_list = [v for v in enron_data['SKILLING JEFFREY K']]
print(feature_list)
for k, v in enron_data.items():
    data_array = featureFormat(v, feature_list)
    labels, features = targetFeatureSplit(data_array)

