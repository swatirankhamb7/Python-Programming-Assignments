#WAP which accepts  one number and prints multiplication table of that number.
#Input :4
#Output :4 8 12 16 20 24 28 32 36 40

def TableofNo(Value):
   for i in range(Value,Value*11,Value):
       print(i,end='   ')#To end line without next line
  
def main():
    print("Enter the number : ")
    No1=int(input())
    print()

    TableofNo(No1)
    
if __name__=="__main__":
    main()