#Write a lambda  which accepts one and return its Cube of that number.
Cube=lambda Value:Value**3

def main():
    print("Enter the number for Calculate the Cube : ")
    Number=int(input())

    Ans=Cube(Number)
    print("Square of a no is : ",Ans)


if __name__=="__main__":
    main()