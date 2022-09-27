import pandas as pd
from sklearn.model_selection import train_test_split
housing=pd.read_csv("housing.csv")
print(housing.head())
y=housing.median_income

x=housing.drop('median_income',axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print("shape of original dataset: ",housing.shape)
print("shape of input training set: ",x_train.shape)
print("shape of output training set: ",y_train.shape)
print("shape of input testing set: ",x_train.shape)
print("shape of output testing set: ",y_train.shape)




