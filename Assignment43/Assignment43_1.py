import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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
    #Step 1 : Load dataset
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load dataset")
    print(Border)
    df=pd.read_csv("PlayPredictor.csv")
    print("Few Records from Dataset is : ")
    print(Border)
    print(df.head())
    print(Border)

    #----------------------------------------------------------------------------------------------------
    #Step 2 : Clean , Prepare and Manipulate the Data
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 2 : Clean , Prepare and Manipulate the Data")
    print(Border)
    print("Shape of Dataset Before Removal Unnamed Columns: ",df.shape)
    print(df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)
    print("Shape of Dataset After Removal Unnamed Columns: ",df.shape)

    le=LabelEncoder()
    df["weather"]=le.fit_transform(df["Whether"])
    df["Temperature"]=le.fit_transform(df["Temperature"])

    X=df[["weather","Temperature"]]
    Y=df["Play"]
    print(Border)


    # #----------------------------------------------------------------------------------------------------
    # #Step 3 : Train the Model
    # #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 3 : Train the Model")
    print(Border)
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
    print("X_train Shape : ",X_train.shape)
    print("X_test Shape : ",X_test.shape)
    print("Y_train Shape : ",Y_train.shape)
    print("Y_test Shape : ",Y_test.shape)

    model=KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,Y_train)
   
   #----------------------------------------------------------------------------------------------------
    #Step 4 : Test Data
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 4 : Test Data")
    print(Border)
    Y_pred=model.predict(X_test)
    
    for i , j in zip(Y_test,Y_pred):
        print("Actual : ",i,"Predicted : ",j)

    #----------------------------------------------------------------------------------------------------
    #Step 5: Calculate Accuracy
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 5: Calculate Accuracy")
    print(Border)
    accuracy=CheckAccuracy(Y_test, Y_pred)
    print("Accuracy is : ",accuracy*100,"%")
    



if __name__=="__main__":
    main()