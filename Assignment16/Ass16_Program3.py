"""WAP which contains one function named as Add() which accepts two numbers from user and return addittion
of that two numbers.
Input :11  5        Output: 16
"""

def Add(Value1,Value2):
    return Value1+Value2

def main():
    print("Enter the First Number : ")
    No1=int(input())

    print("Enter the Second Number : ")
    No2=int(input())
    
    Result=Add(No1,No2)
    print("Addittion is : ",Result)

if __name__=="__main__":
    main()