#WAP which accepts  one number and prints sum of first N natural numbers.
#Input :5
#Output :15

def SumOfN(Value):
   Sum=0
   for i in range(Value+1):
       Sum+=i
   print("Sum of ",Value, "numbers is : ",Sum)
  
def main():
    print("Enter the number : ")
    No1=int(input())
    print()

    SumOfN(No1)
    
if __name__=="__main__":
    main()