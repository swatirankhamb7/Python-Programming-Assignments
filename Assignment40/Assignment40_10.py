"""10. Train model with:
• max_depth = None

Calculate:
• Training accuracy
• Testing accuracy
If training accuracy is 100% but testing accuracy is lower, explain why this happens.
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
    List=["StudyHours",
         "Attendance", 
         "PreviousScore",
         "AssignmentsCompleted",
         "SleepHours"
         ]
    X=df[List]
    Y=df["FinalResult"]
    
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.5,random_state=42)
    model=DecisionTreeClassifier(criterion="gini",max_depth=None,random_state=42)
    model.fit(x_train,y_train)
    y_train_pred=model.predict(x_train)
    y_pred=model.predict(x_test)

    train_accuracy=accuracy_score(y_train,y_train_pred)
    test_accuracy=accuracy_score(y_test,y_pred)

    print("Traning Accuracy : ",train_accuracy*100)
    print("Testing Accuracy : ",test_accuracy*100)

    """
    If training accuracy is 100% but testing accuracy is lower, explain why this happens.?
    Ans: This happen when new data will go for testing .We can say that unknown values for our model these are.
    """


   
if __name__=="__main__":
    main()