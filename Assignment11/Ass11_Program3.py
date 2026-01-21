#WAP which accepts  one number and prints Sum of Digits
#Input :123
#Output :6

def SumDigits(Value):
   Sum=0
   while(Value!=0):
       Sum=Sum+(Value%10)
       Value=int(Value/10)
   return Sum
  
def main():
    print("Enter the number : ")
    No=int(input())
    print()

    Ans=SumDigits(No)
    print("Sum of Digits is : ",Ans)

    
if __name__=="__main__":
    main()