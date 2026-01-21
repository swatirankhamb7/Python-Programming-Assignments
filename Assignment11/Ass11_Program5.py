#WAP which accepts  one number and whether it is pallindrome or not
#Input :123
#Output :321

def CheckPallindrome(Value):
    ValueCopy=Value
    NewValue=0
    while(Value!=0):
        iDigit=Value%10
        NewValue=iDigit+NewValue*10
        Value=int(Value/10)

    if(ValueCopy==NewValue):
        return True
    else:
        return False
  
def main():
    print("Enter the number : ")
    No=int(input())
    print()

    Flag=CheckPallindrome(No)
    if(Flag==True):
        print("Pallindrome")
    else:
        print("Not Pallindrome")

    
if __name__=="__main__":
    main()