#Write a lamda function which accepts Two number and returns Multiplication of that two numbers.
Multiply=lambda Value1,Value2:Value1*Value2

def main():
    print("Enter the number for Multiply : ")
    Number1=int(input())

    print("Enter the Second for Multiply : ")
    Number2=int(input())

    Result=Multiply(Number1,Number2)
    print("Multiplication of  ",Number1,"and ",Number2,"is : ",Result)
    
    
if __name__=="__main__":
    main()