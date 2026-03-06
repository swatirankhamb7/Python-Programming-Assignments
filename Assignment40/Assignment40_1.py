"""1.After training the Decision Tree model, use:
model.feature_importances_
• Display importance score of each feature.
• Which feature contributes the most in predicting FinalResult?
• Which feature contributes the least?"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay)

def main():
    boarder="-"*50
    #step 1 : Dataset loading
    print("Step 1 : load the dataset")
    df=pd.read_csv("student_performance_ml.csv")
    print("Dataset Successfully loaded.......!")
    print(boarder)

    #step 2 : Dataset Analysis
    print("Step 2 : Dataset Analysis")
    #print(df)
    print("Shape of Dataset : ",df.shape)
    print("Column names : ",list(df.columns))
    print()
    print("First Five Records : ")
    print(df.head())
    print()
    print("Last five Records :")
    print(df.tail())
    print("Null Values are : ",df.isnull().sum())
    print(boarder)

   #Visualization
    print("Step 3 : Data Visualization : ")
    sns.scatterplot(x=df["StudyHours"],y=df["FinalResult"],hue=df["FinalResult"])
    plt.title("Relationship between Study Hours and Final Result")
    plt.xlabel("Study Hours")
    plt.ylabel("Final Result")
    plt.show()

    #Train_test_split
    List=["StudyHours",
         "Attendance", 
         "PreviousScore",
         "AssignmentsCompleted",
         ]
    X=df[List]
    Y=df["FinalResult"]
    print(boarder)

    print("step 4 : Train test split")
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    print("Size of X train : ",x_train.shape)
    print("Size of X test : ",x_test.shape)
    print("Size of Y train : ",y_train.shape)
    print("Size of Y test : ",y_test.shape)
    print(boarder)

    #Model training
    print("Step 5 : Model Traning")
    model=DecisionTreeClassifier(max_depth=100)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    print(boarder)

    #Accuracy Calculation : To Evaluate the performance of model
    print("Step 6 : Accuracy Calculation")
    accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy Score  : ",accuracy*100)
    print(boarder)

    importances=model.feature_importances_
    feature_importances=pd.Series(importances,index=X.columns)
    feature_importances.nlargest(10).plot(kind="barh")
    plt.show()
    """Study hours factor contributing mostly in predicting Final Result.
     rather than Study hours other factors contibutes the least. """


if __name__=="__main__":
    main()