#WAP which accepts  one number and prints Cube of that number.

def Cube(Value1):
    return Value1**3



def main():
    print("Enter the number : ")
    No1=int(input())

    Ans=Cube(No1)
    print("Cube of given no is : ",Ans)

if __name__=="__main__":
    main()