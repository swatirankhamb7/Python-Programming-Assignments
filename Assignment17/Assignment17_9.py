'''WAP  which accept one number from user and return number of digits in that Number.
  Input:5187934
  Output:7
  
'''
def CountDigit(n):
    Count=0
    while(n!=0):
        n=int(n/10)  
        Count+=1
    return Count  
def main():
    print("Enter the Number : ")
    No=int(input())

    Result=CountDigit(No)
    print("No of Digit in ",No,"is : ",Result)
        
if __name__=="__main__":
    main()