#Write a lamda function which accepts one  number and returns True if number is Odd otherwise False.
IsOdd=lambda Value:Value%2!=0

def main():
    print("Enter the number to check number is Odd : ")
    Number=int(input())

    Result=IsOdd(Number)
    print(Number," is Odd Number : ",Result)
    
if __name__=="__main__":
    main()