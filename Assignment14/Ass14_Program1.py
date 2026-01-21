#Write a lambda  which accepts one and return its square of that number.
Square=lambda Value:Value**2

def main():
    print("Enter the number for Calculate the square : ")
    Number=int(input())

    Ans=Square(Number)
    print("Square of a no is : ",Ans)


if __name__=="__main__":
    main()