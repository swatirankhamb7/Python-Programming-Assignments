#WAP which accepts  one number and checks whether if it is divisible by 3 and 5.
#Input :15
#Output : Divisible by 3 and 5.

def CheckDivisible(Value):
    if(Value%3==0 and Value%5==0):  #&& : Not in python As we use in C,C++,Java
        print("Divisible by 3 and 5 .")
    else:
        print("Not Divisible by 3 and 5 .")

    
def main():
    print("Enter the number : ")
    No1=int(input())

    CheckDivisible(No1)
    

if __name__=="__main__":
    main()