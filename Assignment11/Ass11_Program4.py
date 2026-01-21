#WAP which accepts  one number and prints Reverse of that no
#Input :123
#Output :321

def ReverseNo(Value):
   NewValue=0
   while(Value!=0):
       iDigit=Value%10
       NewValue=iDigit+NewValue*10
       Value=int(Value/10)
   return NewValue
  
def main():
    print("Enter the number : ")
    No=int(input())
    print()

    Ans=ReverseNo(No)
    print("Reverse Number  is : ",Ans)

    
if __name__=="__main__":
    main()