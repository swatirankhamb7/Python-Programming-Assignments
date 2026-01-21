#WAP which accepts  one number and check whether it is prime or not
#Input :11
#Output :Prime Number

def CheckPrime(Value):
   if(Value==1 or Value==0):
       return False
   for i in range(2,int(Value/2)):
       if(Value%i==0):
           return False
   return True
  
def main():
    print("Enter the number : ")
    No=int(input())
    print()

    Flag=CheckPrime(No)
    if(Flag==True):
        print("Prime number")
    else:
        print("Not a Prime Number")

    
if __name__=="__main__":
    main()