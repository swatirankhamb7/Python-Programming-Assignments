
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


def main():
    Border="-"*50
    #----------------------------------------------------------------------------------------------------
    #Step 1 : Load dataset
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load dataset")
    print(Border)
    df=pd.read_csv("Advertising.csv")
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
    if 'Unnamed: 0' in df.columns:
        df.drop(columns='Unnamed: 0',inplace=True)
    print("Shape of Dataset After Removal Unnamed Columns: ",df.shape)
    print("Clean Dataset is :")
    print(Border)
    print(df.head())
    print(Border)

    #----------------------------------------------------------------------------------------------------
    #Step 3 : Train the Model
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 3 : Train the Model")
    print(Border)
    X=df[["TV","radio","newspaper"]]
    Y=df["sales"]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)
    print("X_train Shape : ",X_train.shape)
    print("X_test Shape : ",X_test.shape)
    print("Y_train Shape : ",Y_train.shape)
    print("Y_test Shape : ",Y_test.shape)

    model=LinearRegression()
    model.fit(X_train,Y_train)
   
    #----------------------------------------------------------------------------------------------------
    #Step 4 : Test Data
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 4 : Test Data")
    print(Border)
    Y_pred=model.predict(X_test)
    
    #----------------------------------------------------------------------------------------------------
    #Step 5: Display Predicted and Actual Values
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 5: Display Predicted and Actual Values")
    print(Border)
    for i , j in zip(Y_test,Y_pred):
        print("Actual : ",i,"    ","Predicted : ",j)
    print(Border)

    #----------------------------------------------------------------------------------------------------
    #Step 6 : Evaluate the Model
    #----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 6 : Evaluate the Model")
    print(Border)
    MSE=mean_squared_error(Y_test,Y_pred)
    print("MSE : ",MSE)
    R_Squared_Error=r2_score(Y_test,Y_pred)
    print("R_Square Error : ",R_Squared_Error)
    print(Border)


if __name__=="__main__":
    main()