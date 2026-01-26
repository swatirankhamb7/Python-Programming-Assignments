'''
Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for 
subtraction,Mult() for multiplication and Div() for division. All functions accepts two parameters as number
and perform the operation. Write on python program which call all the functions from Arithmetic module by 
accepting the parameters from use
'''
from Arithmetic import Add,Sub,Mult,Div

def main():
    print("Enter the First Number : ")
    No1=int(input())

    print("Enter the Second Number : ")
    No2=int(input())

    print("Addittion : ",Add(No1,No2))
    print("Subtraction : ",Sub(No1,No2))
    print("Multiplication : ",Mult(No1,No2))
    print("Division : ",Div(No1,No2))
    
if __name__=="__main__":
    main()