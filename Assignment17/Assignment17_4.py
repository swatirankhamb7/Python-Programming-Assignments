'''WAP  which accept one number from user and returns addittion of its factors.
   Input:12
   Output:16 (1+2+3+4+6)
'''
def SumFactors(n):
    Sum=0
    for i in range(1,int(n/2+1)):
        if(n%i==0):
            Sum+=i
    return Sum
    
def main():
    print("Enter the Number to find its Sum of Factors : ")
    No=int(input())
    Result=SumFactors(No)
    print("Sum of Factors of  ",No," is : ",Result)
    
if __name__=="__main__":
    main()