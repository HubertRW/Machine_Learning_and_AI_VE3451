# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:31:31 2026

@author: huber
"""

import pandas as pd
from sqlalchemy import select, create_engine
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder



training_data = pd.read_csv('Network Intrusion Detection- UNSW_NB15 training and testing sets/UNSW_NB15_training-set.csv',
                            sep=",")

columns = training_data.columns
attacks = training_data.query("label > 0")

testing_set = pd.read_csv('Network Intrusion Detection- UNSW_NB15 training and testing sets/UNSW_NB15_testing-set.csv', sep=",")

#print(attacks)

print(testing_set)
