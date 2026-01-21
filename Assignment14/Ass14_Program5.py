#Write a lamda function which accepts one  number and returns True if number is even otherwise False.
IsEven=lambda Value:Value%2==0

def main():
    print("Enter the number to check number is Even : ")
    Number=int(input())

    Result=IsEven(Number)
    print(Number," is Even Number : ",Result)
    
if __name__=="__main__":
    main()