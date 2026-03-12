import pandas as pd
def mean(X):
    Sum=0
    for i in X:
        Sum+=i
    X_Bar=Sum/len(X)
    return X_Bar

def CalculationM(X,Y,X_Bar,Y_Bar):
    Sum_X_Y_Bar=0
    Sum_X_dev=0

    for i,j in zip(X,Y):
        dev_X=i-X_Bar
        dev_X_Y=dev_X*(j-Y_Bar)
        Sum_X_Y_Bar +=dev_X_Y
        Square=(dev_X)**2
        Sum_X_dev +=Square

    m=Sum_X_Y_Bar/Sum_X_dev
    return m

def CalculateIntercept(m,X_Bar,Y_Bar):
    C=Y_Bar-m*X_Bar
    return C

def CalculateEquation(m,C):
    m=str(m)
    C=str(C)
    Equation=""
    Equation="Y"+"="+m+"X"+"+"+C
    return Equation

def CalculatePrediction(m,C,X):
    y_pred=[]
    for x in X: 
     y=m*x+C
     y_pred.append(y)
    return y_pred

def CalculateR2(Y_Bar,Y_pred,Y):
    R2=0
    Numerator=0
    Denominator=0

    for i,j in zip(Y,Y_pred):
        dev_Yp=j-Y_Bar
        Numerator+=(dev_Yp)**2
        dev_Y=i-Y_Bar
        Denominator+=(dev_Y)**2
    
    R2=Numerator/Denominator
    return R2

def CalculateMSE(Y,Y_pred):
    MSE=0
    n=len(Y)
    Sum=0

    for i,j in zip(Y,Y_pred):
       diff=i-j
       Sum+=diff**2
    
    MSE=(1/n) * Sum
    return MSE

    
def main():
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    X_Bar=mean(X)
    Y_Bar=mean(Y)

    print("Mean of X: ",X_Bar)
    print("Mean of Y: ",Y_Bar)

    Slope=CalculationM(X,Y,X_Bar,Y_Bar)
    print("Slope (m) : ",Slope)

    Intercept=CalculateIntercept(Slope,X_Bar,Y_Bar)
    print("Intercept (C) : ",Intercept)
    
    Regression_Equation=CalculateEquation(Slope,Intercept)
    print("Regression Equation : \n",Regression_Equation)

    Y_pred=CalculatePrediction(Slope,Intercept,X)
    dataX={"Actual":Y,
          "Predict":Y_pred
          }
    data=pd.DataFrame(dataX)
    print(data)

    R2=CalculateR2(Y_Bar,Y_pred,Y)
    MSE=CalculateMSE(Y,Y_pred)
    print("Mean Squared Error : ",MSE)
    print("R2 Score : ",R2)
        
if __name__=="__main__":
    main()