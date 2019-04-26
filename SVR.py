# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:08:07 2019

@author: diana
"""
# import libraries
import numpy as np
import pandas as pd
import matplotlib as plt

# import dataset
df = pd.read_csv('Position_Salaries.csv')
x = df.iloc[:,1]
y = df.iloc[:,2]

# feature scale prodecure
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(x)
Y = sc.fit_transform(y)

# train the SVR model
from sklearn.svm import SVR
model = SVR(kernel = "rbf")
model,fit(X, Y)

# predict the 
