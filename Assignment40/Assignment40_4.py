"""
4. Create a new DataFrame with details of 5 new students.
   Use the trained model to predict their results.
   Display predictions clearly.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay)

def main():
    
    df=pd.read_csv("student_performance_ml.csv")

    List=["StudyHours",
         "Attendance", 
         "PreviousScore",
         "AssignmentsCompleted",
         "SleepHours"
         ]
    X=df[List]
    Y=df["FinalResult"]

   #New Dataframe
    new_Student_Data=[
        {"StudyHours":10,"Attendance":82,"PreviousScore":50,"AssignmentsCompleted":7,"SleepHours":5},
        {"StudyHours":2,"Attendance":82,"PreviousScore":50,"AssignmentsCompleted":7,"SleepHours":8},
        {"StudyHours":5,"Attendance":50,"PreviousScore":70,"AssignmentsCompleted":4,"SleepHours":7},
        {"StudyHours":0,"Attendance":100,"PreviousScore":40,"AssignmentsCompleted":2,"SleepHours":6},
        {"StudyHours":3,"Attendance":60,"PreviousScore":65,"AssignmentsCompleted":5,"SleepHours":7},
    ]
    new_Data=pd.DataFrame(new_Student_Data)
    
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)


    #Model training
    
    model=DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=42)
    model.fit(x_train,y_train)
    y_pred=model.predict(new_Data)
    #Display Predictions :
    print("Predictions are as follws : ")
    for i in y_pred:
        print(i)
    
if __name__=="__main__":
    main()