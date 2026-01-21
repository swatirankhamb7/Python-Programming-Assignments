#WAP which accepts  one number and prints count of digits in that number
#Input :7521
#Output :Prime Number

def CountDigits(Value):
   Count=0
   while(Value!=0):
       Count+=1
       Value=int(Value/10)
   return Count
  
def main():
    print("Enter the number : ")
    No=int(input())
    print()

    Ans=CountDigits(No)
    print("Count of Digits is : ",Ans)

    
if __name__=="__main__":
    main()