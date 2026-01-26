'''WAP  which accept one number from user and returns its factorial.
   Input:5
   Output:120
'''
def Factorial(n):
    if(n==0 or n==1):
        return 1
    else:
       return n*Factorial(n-1)
    
def main():
    print("Enter the Number to find Factorial : ")
    No=int(input())
    Result=Factorial(No)
    print("Factorial of ",No," is : ",Result)
   
if __name__=="__main__":
    main()