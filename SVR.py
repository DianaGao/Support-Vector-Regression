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

# visualize the scaling 
plt.scatter(x, y , c = "orange")
plt.scatter(X, Y, c  = "red")
plt.title("Scatter of the Level VS salary")
plt.xlabel("Salary")
plt.ylabel("Level")
plt.show()

# train the SVR model
from sklearn.svm import SVR
model = SVR(kernel = "rbf")
model.fit(X, Y)

# predict the salary
y_pred = model.predict(sc_x.fit_transform(6.5))
y_pred2 = sc_y.inverse_transform(y_pred)

# Create the data visualization of the scaled dataset
plt.scatter(X, Y , c = "red")
plt.plot(X, model.predict(X) , c = "blue")
plt.title("SVR model")
plt.xlabel("Salary")
plt.ylabel("Level")
plt.show()

# Create the visualization of the orifinal dataset
plt.scatter(x, y , c = "orange")
plt.title("Scatter of the Level VS salary")
plt.xlabel("Salary")
plt.ylabel("Level")
plt.show()
