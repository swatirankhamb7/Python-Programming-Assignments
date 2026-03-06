"""7. Train model using:
• random_state = 0
• random_state = 10
• random_state = 42
Compare testing accuracy.
Does the result change?
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
    #random state :0
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
    model=DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=0)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy is when Random state is 0 : ",accuracy*100)

    #random state :10
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=10)
    model=DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=10)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy is when Random state is 10 : ",accuracy*100)

    #random state :42
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    model=DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=42)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy is when Random state is 42 : ",accuracy*100)

    "Yes the Result Changes."

if __name__=="__main__":
    main()