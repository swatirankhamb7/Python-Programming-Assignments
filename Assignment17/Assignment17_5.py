'''WAP  which accept one number from user and check whether no is Prime or not
   Input:5
   Output:It is Prime Number
'''
def CheckPime(n):
    Flag=True
    for i in range(2,n):
        if(n%i==0):
            return False
    return Flag
    
def main():
    print("Enter the Number to Check is it Prime or not  : ")
    No=int(input())
    Result=CheckPime(No)
    if(Result==True):
        print("It is Prime number.")
    else:
        print("It is not Prime Number")
 
if __name__=="__main__":
    main()