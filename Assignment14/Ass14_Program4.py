#Write a lambda  which accepts two number and return minimum number.
Cube=lambda Value1,Value2:Value1<Value2

def main():
    print("Enter the First number : ")
    Number1=int(input())

    print("Enter the Second number : ")
    Number2=int(input())

    Flag=Cube(Number1,Number2)

    if Flag==True:
        print(Number1,"is Smallest")
    else:
        print(Number2,"is Smallest")
    
    
if __name__=="__main__":
    main()