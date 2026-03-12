import matplotlib.pyplot as plt
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
    y_pred=m*X+C
    return y_pred
    
def main():
    Experience=[1,2,3,4,5]
    Salary=[20000,25000,30000,35000,40000]

    X_Bar=mean(Experience)
    Y_Bar=mean(Salary)

    print("Mean of X: ",X_Bar)
    print("Mean of Y: ",Y_Bar)

    Slope=CalculationM(Experience,Salary,X_Bar,Y_Bar)
    print("Slope (m) : ",Slope)

    Intercept=CalculateIntercept(Slope,X_Bar,Y_Bar)
    print("Intercept (C) : ",Intercept)
    
    Regression_Equation=CalculateEquation(Slope,Intercept)
    print("Regression Equation : \n",Regression_Equation)

    Predicted_Value=CalculatePrediction(Slope,Intercept,X=6)
    print(f"Predicted Y for X=6 : ",Predicted_Value)
   
    plt.figure(figsize=(8,8))
    plt.plot(Experience,Salary,color="g",label='Regression Line ')
    plt.scatter(Experience,Salary,color="r",label="Scatter Plot")
    plt.xlabel("X : Experience(Independent Variable)")
    plt.ylabel("Y : Salary (Dependent Vaiable )")
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()