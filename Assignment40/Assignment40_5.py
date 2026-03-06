"""5. Without using accuracy_score, manually calculate accuracy:
Verify whether it matches sklearn accuracy.

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
    
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)


    #Model training
    
    model=DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=42)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    #Display Predictions :
    Count=0
    print("Predictions and Actual Comparison is  as follws : ")
    for i , j in zip(y_pred,y_test):
        print("Actual : ",j,"  ","Prediced : ",i)
        if(i==j):
            Count+=1

    #Accuracy Check
    accuracy1=accuracy_score(y_test,y_pred)
    print("Accuracy 1 is : ",accuracy1*100)
    accuracy2=Count/len(y_pred)*100
    print("Accuracy 2 is : ",accuracy2)
    
if __name__=="__main__":
    main()