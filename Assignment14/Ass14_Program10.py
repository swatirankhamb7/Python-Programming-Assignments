#Write a lamda function which accepts Three number and returns Largest of that three numbers.
Largest=lambda A,B,C:A if (A>B and A>C) else B if (B>A and B>C) else C

def main():
    print("Enter the number: ")
    Number1=int(input())

    print("Enter the Second Number ")
    Number2=int(input())

    print("Enter the Third Number")
    Number3=int(input())

    Result=Largest(Number1,Number2,Number3)
    print(Result)
    print(Result,"is the Largest")
    
    
if __name__=="__main__":
    main()