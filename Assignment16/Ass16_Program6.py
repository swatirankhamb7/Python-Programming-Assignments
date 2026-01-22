"""WAP which accept number and check whether that  number is given positive or negative or zero
Input : 11      Output :Positive Number
Input : -8      Output :Negative Number
Input : 11      Output :Zero
"""
def CheckNumber(no):
    if(no>0):
        print("Positive Number")
    elif(no<0):
        print("Negative Number")
    elif(no==0):
        print("Zero")
    
def main():
    print("Enter the Number : ")
    no=int(input())
    print()

    CheckNumber(no)

if __name__=="__main__":
    main()