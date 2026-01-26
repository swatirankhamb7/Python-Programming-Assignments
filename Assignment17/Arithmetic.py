def Add(Num1,Num2):
    return Num1+Num2

def Sub(Num1,Num2):
    return Num1-Num2

def Mult(Num1,Num2):
    return Num1*Num2

def Div(Num1,Num2):
    try:
       return Num1/Num2
    
    except Exception as eobj:
        print("Inside Except : ",eobj)
