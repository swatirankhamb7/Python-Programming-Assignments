import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay)

def main():
    #1.
    """
    1. Import DecisionTreeClassifier from sklearn.**
    Create a model object and train it using `fit()`
    """
    df=pd.read_csv("student_performance_ml.csv")
    feature_cols=["StudyHours","Attendance","AssignmentsCompleted","SleepHours"]
    X=df[feature_cols]
    Y=df["FinalResult"]

    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    model=DecisionTreeClassifier(criterion="gini",max_depth=3,random_state=42)
    model.fit(x_train,y_train)
   
   #2.  """
    """**2. Use the trained model to predict results for X_test.**
    Display predicted values along with actual values."""

    res=model.predict(x_test)
    real_array=np.array(y_test)
    pred_array=np.array(res)
    df_comaprion=pd.DataFrame({"Actual": real_array.flatten(),
                      "Predicted":pred_array.flatten()})
    print(df_comaprion)

   #3 
    """**3. Calculate model accuracy using `accuracy_score`.**
    Display the result in percentage format"""

    Accuracy=accuracy_score(y_test,res)
    print(f"Accuracy Percent is : {Accuracy*100}")

    #4
    """4. Generate confusion matrix using sklearn.**
    Display it using `ConfusionMatrixDisplay`.

    Explain clearly:
    * True Positive
    * True Negative
    * False Positive
    * False Negative"""

    cm=confusion_matrix(y_test,res)
    print("Confusion Matrix : ")
    print(cm)
    """
    1.True Positive : Predicted Correct | Actual Correct
    2.True Negative : Predicted Incorrect |Acual Incorrect
    3.False positive : Predicted Correct | Actual Incorrect
    4.False Negative : Predicted Incorrect | Actual Correct
    """

    #5.
    """5. Calculate:
    Training accuracy
    Testing accuracy
    Compare both and comment whether the model is overfitting or underfitting."""
    train_accuracy = model.score(x_train, y_train)
    test_accuracy = model.score(x_test, y_test)

    print(f"Training Accuracy: {train_accuracy * 100:.2f}%")
    print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")
    """Given Model is not overfitted or underderfitted because both trainig and testing accurcay is same"""

   #6.
    """ Train three Decision Tree models with:
    max_depth = 1
    max_depth = 3
    max_depth = None
    Compare their testing accuracies and write your observations."""

    #Max_depth=1
    print("While Max_depth =1")
    model=DecisionTreeClassifier(criterion="gini",max_depth=1,random_state=42)
    model.fit(x_train,y_train)
    res=model.predict(x_test)
    Accuracy=accuracy_score(y_test,res)
    print(f"Accuracy Percent is : {Accuracy*100}")
    print()

    #Max_depth=2
    print("While Max_depth =2")
    model=DecisionTreeClassifier(criterion="gini",max_depth=2,random_state=42)
    model.fit(x_train,y_train)
    res=model.predict(x_test)
    Accuracy=accuracy_score(y_test,res)
    print(f"Accuracy Percent is : {Accuracy*100}")
    print()

    #Max_depth=3
    print("While Max_depth =3")
    model=DecisionTreeClassifier(criterion="gini",max_depth=3,random_state=42)
    model.fit(x_train,y_train)
    res=model.predict(x_test)
    Accuracy=accuracy_score(y_test,res)
    print(f"Accuracy Percent is : {Accuracy*100}")
    print()


  #7.
    """7. Use the trained model to predict result for a student with:
    StudyHours = 6
    Attendance = 85
    PreviousScore = 66
    AssignmentsCompleted = 7
    SleepHours = 7
    Will the student Pass or Fail?"""

    user_data=pd.DataFrame([{"StudyHours":6,"Attendance":85,"AssignmentsCompleted":7,"SleepHours":7,}])
    res=model.predict(user_data)
    print(res)

    """Student will pass in the examination"""


if __name__=="__main__":
    main()