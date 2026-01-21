#WAP which contains one number and prints square of that number.
#Input : 5
#Output : 25

def Square(Value1):
    return Value1**2


def main():
    print("Enter the number : ")
    No1=int(input())

    Ans=Square(No1)
    print("Square of given no is : ",Ans)

if __name__=="__main__":
    main()