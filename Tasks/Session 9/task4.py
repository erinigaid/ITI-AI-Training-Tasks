import pandas as pd
import numpy as np

dataset=pd.read_csv('Breast_cancer_data.csv')
# print(dataset.shape)
x=pd.DataFrame(dataset.iloc[:,:-1])
y=pd.DataFrame(dataset.iloc[:,-1])
# print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.linear_model import  LogisticRegression
logmodel=LogisticRegression()
logmodel.fit(x_train,np.ravel(y_train))
y_pred=logmodel.predict(x_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

from sklearn.metrics import confusion_matrix
confusion_matrix=confusion_matrix(y_test,y_pred)
print(confusion_matrix)





