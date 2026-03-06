"""8. Decision Tree Visualization
Use:
from sklearn.tree import plot_tree
Visualize the trained decision tree.
• Which feature appears at the root node?
• Why do you think that feature was selected first?
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

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
    model=DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=42)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)
    

    plt.figure(figsize=(10,10))
    plot_tree(model,max_depth=3,filled=True,feature_names=["StudyHours",
         "Attendance", 
         "PreviousScore",
         "AssignmentsCompleted",
         "SleepHours"],class_names=["0","1"])
    plt.title("Decision Tree Visualization")
    plt.show()
    """Attendance Feature Appears on root node.
    I think Attendance may affect Final Performance thats why they taken Attendance Feature on root node.
    """

   
if __name__=="__main__":
    main()