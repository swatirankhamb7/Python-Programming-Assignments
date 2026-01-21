#WAP which accepts one number and print binary equivalent  
def BinaryResult(Value):
    Res=''
    while(Value>0):
        Res=str(Value%2)+Res
        Value//=2
    print(Res)

def main():
    print("Enter the Number to find the binary : ")
    no=int(input())
    print()
    BinaryResult(no)


if __name__=="__main__":
    main()