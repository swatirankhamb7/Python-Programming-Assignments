#Write a lamda function which accepts Two number and returns Addittion of that two numbers.
Add=lambda Value1,Value2:Value1+Value2

def main():
    print("Enter the number for Addittion : ")
    Number1=int(input())

    print("Enter the Second for Addittion : ")
    Number2=int(input())

    Result=Add(Number1,Number2)
    print("Addittion of ",Number1,"and ",Number2,"is : ",Result)
    
    
if __name__=="__main__":
    main()