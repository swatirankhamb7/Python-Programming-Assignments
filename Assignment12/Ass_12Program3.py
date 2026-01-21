#WAP which accepts two numbers and prints Addittion,Substraction,Multiplication and Division

def Calculator(Value1,Value2):
    Add=Value1+Value2
    Sub=Value1-Value2
    Mul=Value1*Value2
    Div=Value1/Value2
    return Add,Sub,Mul,Div
  
def main():
    print("Enter the First number : ")
    No1=int(input())
    print("Enter the Second number : ")
    No2=int(input())
    print()
    
    Add,Sub,Mul,Div=Calculator(No1,No2)
    print("Addittion : ",Add)
    print("Substraction : ",Sub)
    print("Multiplication : ",Mul)
    print("Division : ",Div)
if __name__=="__main__":
    main()