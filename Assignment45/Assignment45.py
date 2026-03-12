
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

def CheckAccuracy(Y_test,Y_Pred):
    CorrectCount=0
    WrongCount=0
    for i,j in zip(Y_test,Y_Pred):
        if(i==j):
            CorrectCount+=1
    
    Ans=CorrectCount/len(Y_test)
    return Ans

def main():
    Border="-"*50
    #----------------------------------------------------------------------------------------------------
    # Step 1 : Load dataset
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load dataset")
    print(Border)
    df=pd.read_csv("WinePredictor.csv")
    print("Few Records from Dataset is : ")
    print(Border)
    print(df.head())
    cols=list(df.columns)
    print("Columns Names are : ",cols)
    print(Border)

    #----------------------------------------------------------------------------------------------------
    # Step 2 : Clean , Prepare and Manipulate the Data
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 2 : Clean , Prepare and Manipulate the Data")
    print(Border)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns='Unnamed: 0',inplace=True)
    print("Shape of Dataset is : ",df.shape)
    print("Total Columns : ",df.shape[1])
    print("Total Rows : ",df.shape[0])
    print(Border)

    #----------------------------------------------------------------------------------------------------
    # Step 3 : Train the Model
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 3 : Train the Model")
    print(Border)
    X=df.drop(columns=["Class"])
    Y=df["Class"]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
    print("X_train Shape : ",X_train.shape)
    print("X_test Shape : ",X_test.shape)
    print("Y_train Shape : ",Y_train.shape)
    print("Y_test Shape : ",Y_test.shape)
    Scalar=StandardScaler()
    X_train_Scaled=Scalar.fit_transform(X_train)
    X_test_Scaled=Scalar.fit_transform(X_test)



    model=KNeighborsClassifier(n_neighbors=9)
    model.fit(X_train_Scaled,Y_train)
   
    #----------------------------------------------------------------------------------------------------
    # Step 4 : Test Data
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 4 : Test Data")
    print(Border)
    Y_pred=model.predict(X_test_Scaled)
    
    #----------------------------------------------------------------------------------------------------
    # Step 5: Display Predicted and Actual Values
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 5: Display Predicted and Actual Values")
    print(Border)
    for i , j in zip(Y_test,Y_pred):
        print("Actual : ",i,"    ","Predicted : ",j)
    print(Border)

    #----------------------------------------------------------------------------------------------------
    # Step 6 : Check Accuracy
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 6: Calculate Accuracy")
    print(Border)
    accuracy=CheckAccuracy(Y_test, Y_pred)
    print("Accuracy is : ",accuracy*100,"%")

    


if __name__=="__main__":
    main()