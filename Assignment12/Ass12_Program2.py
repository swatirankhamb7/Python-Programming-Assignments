#WAP which accepts  one number and print its factors
#Input:12
#Output :1 2 3 4 6 12

def Factors(Value):
    for i in range(1,Value+1):
        if(Value%i==0):
            print(i,end=" ")
  
def main():
    print("Enter the number : ")
    No=int(input())
    print()
    Factors(No)
if __name__=="__main__":
    main()