'''
2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.

Input : 4 3   Output : 12
Input : 6 3   Output : 18
'''
Multiplication=lambda A,B:A*B
def main():
    print("Enter the first number : ")
    no1=int(input())

    print("Enter the Second number : ")
    no2=int(input())

    Result=Multiplication(no1,no2)
    print("Product os  ",no1,"and",no2,"is : ",Result)

if __name__=="__main__":
    main()