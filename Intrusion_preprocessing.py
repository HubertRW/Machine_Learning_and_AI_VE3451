# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:31:31 2026

@author: huber
"""

import pandas as pd
#from sqlalchemy import select, create_engine
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_classif



training_data = pd.read_csv('Network Intrusion Detection- UNSW_NB15 training and testing sets/UNSW_NB15_training-set.csv',
                            sep=",")
testing_set = pd.read_csv('Network Intrusion Detection- UNSW_NB15 training and testing sets/UNSW_NB15_testing-set.csv', 
                          sep=",")

columns = training_data.columns
attacks = training_data.query("label == 1") 
training_full = training_data.dropna()


#print("Records without missing features: ")
#print(training_full)

#print("total features: ")
#print(columns)

#print("Packets to and from the same device & port: ")
#print(training_data.query("is_sm_ips_ports > 0"))

#print(attacks)
#print(testing_set)


# Top 15 best features(can reduce this later on)

altered_training = training_data.drop(["id","proto","state","service"], axis=1)

y = altered_training.iloc[:,-1] # we're choosing the "label" column as the target
X = altered_training.iloc[:,0:39]

features = SelectKBest(score_func=f_classif, k=15)
features.fit_transform(X, y)

indices = features.get_support()
selected = X.columns[indices]

scores = pd.DataFrame({"Feature": selected,  
    "Score": features.scores_[indices]}
)

scores = scores.sort_values(by="Score", ascending=False)
scores.index = pd.RangeIndex(start=1, stop=len(scores)+1, step=1)

print("Top 15 Features: ")
print(scores)

#print("Altered dataset: ")
#print(altered_training)
