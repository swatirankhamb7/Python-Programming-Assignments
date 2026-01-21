#WAP which accepts one number and prints that many numbers in Reverse
#Input :5
#Output :5 4 2 2 1

def ReverseN(Value):
   for i in range(Value,0,-1):
       print(i,end=" ") 
def main():
    print("Enter the number : ")
    No=int(input())

    ReverseN(No)
    
if __name__=="__main__":
    main()