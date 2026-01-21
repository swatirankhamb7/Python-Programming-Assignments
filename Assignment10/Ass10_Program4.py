#WAP which accepts  one number and prints all even numbers till that no
#Input :10
#Output :2 4 6 8 10

def EvenNo(Value):
   for i in range(1,Value+1):
       if(i%2==0):
           print(i,end=" ")
  
def main():
    print("Enter the number : ")
    No1=int(input())
    print()

    EvenNo(No1)

    
if __name__=="__main__":
    main()