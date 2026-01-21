#WAP which accepts  one number and prints Factorial of that no
#Input :5
#Output :120

def Factorial(Value):
   fact=1
   for i in range(1,Value+1):
       fact=i*fact
   return fact
  
def main():
    print("Enter the number : ")
    No1=int(input())
    print()

    Ans=Factorial(No1)
    print("Factorial of given no is : ",Ans)
    
if __name__=="__main__":
    main()