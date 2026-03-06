"""9. Create a new column:
PerformanceIndex = (StudyHours * 2) + Attendance
Train the model including this new feature.
Does accuracy improve?
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score

def main():
    
    df=pd.read_csv("student_performance_ml.csv")

    for i in df:
        df["PerformanceIndex"]=df["StudyHours"]*2+df["Attendance"]
    print(df)
    List=["StudyHours",
         "Attendance", 
         "PreviousScore",
         "AssignmentsCompleted",
         "SleepHours",
         "PerformanceIndex"
         ]
    X=df[List]
    Y=df["FinalResult"]
    
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    model=DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=42)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy Score : ",accuracy*100)


   
if __name__=="__main__":
    main()