"""WAP which contains one function that accept one number from user and returns true if numbers 
is divisible by 5 otherwise  retuen False
Input : 8      Output :False
Input : 25     Output :True

"""
def CheckDivisible(no):
    if(no%5==0):
        return True
    else:
        return False
    
def main():
    print("Enter the Number : ")
    no=int(input())
    print()
    Result=CheckDivisible(no)
    print("Is ",no,"is divisible by 5 : ",Result)

if __name__=="__main__":
    main()