#WAP which accepts  one number and prints all odd numbers till that no

def OddNo(Value):
   for i in range(1,Value+1):
       if(i%2!=0):
           print(i,end=" ")
  
def main():
    print("Enter the number : ")
    No1=int(input())
    print()

    OddNo(No1)

    
if __name__=="__main__":
    main()