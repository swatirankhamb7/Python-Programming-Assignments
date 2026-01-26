'''WAP  which accept one number from user and return number of digits in that Number.
  Input:5187934
  Output:7
  
'''
def CountDigit(n):
    Sum=0
    while(n!=0):
        Sum=Sum+(n%10)
        n=int(n/10)
    return Sum  
def main():
    print("Enter the Number : ")
    No=int(input())

    Result=CountDigit(No)
    print("Sum of Digits of ",No,"is : ",Result)
        
if __name__=="__main__":
    main()