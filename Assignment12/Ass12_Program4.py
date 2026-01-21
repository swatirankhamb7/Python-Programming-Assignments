#WAP which accepts one number and prints that many numbers starting from 1
#Input :1
#Output :1 2 3 4 5

def PrintNumbers(Value):
   for i in range(1,Value+1,1):
       print(i,end=" ") 
def main():
    print("Enter the number : ")
    No=int(input())

    PrintNumbers(No)
    
if __name__=="__main__":
    main()