"""6. Identify students where:
y_test  !=  y_pred
• Display those rows.
• How many students were misclassified?
• What common pattern do you observe?
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
    
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.5,random_state=42)


    #Model training
    
    model=DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=42)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
   
    print("Missclassified Entries are :  ")
    for i , j in zip(y_pred,y_test):
        if(i==j):
            pass
        else:
            print("Actual : ",j,"  ","Prediced : ",i)

    accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy is : ",accuracy*100)

if __name__=="__main__":
    main()