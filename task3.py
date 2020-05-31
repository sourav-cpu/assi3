import numpy as np
import pandas as pd
df.pd.read_csv("student_math.csv")
from sklearn preprocessing import labelEncoder
labelencoder = Labelencoder()
x[:,9]=labelencoder.fit.transform(x[:,9])
x[:,10]=labelencoder.fit.transform(x[:,10])
x[:,11]=labelencoder.fit.transform(x[:,11])
x[:,12]=labelencoder.fit.transform(x[:,12])
df["final_grade"]=df["G1"]+df["G2"]+df["G3"]
y=np.asarray(df["final grade"]
x=df["school"],df["sex"],df["age"],df["address"],df["famsize"],df["pstatus"],df["medu"],df["fedu"],df["mjob"],df["fjob"],df["reason"],df["guardian"],df["traveltime"],df["studytime"],df["failure"],df["schoolsup"],df["famsup"],df["paid"],df["activities"],df["nusery"],df["higher"],df["internet"],df["romantic"],df["famrel"],df["freetime"],df["goout"],df["dalc"],df["walc"],df["health"],df["absences"],df["g1"],df["g2"]
from sklearn.model_selection
import train_test_split
x_train , x-test , y_train , y_test = train_test_split(x , y , test_size=0.2)
from sklearn.linear_model import
LinearRegression
from sklearn import metrics
from sklearn.cross_validation
import train_test_split
regressor=LinearRegression
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_test)
from sklearn.metrics import
confusion_matrix
cm=confusion_matrix(y_test,y_pred)
import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred,s=None,c=None)
             
