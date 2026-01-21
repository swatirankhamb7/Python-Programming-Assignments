#WAP which accepts one number and checks whether it is perfect no or not.
#Input :6
#Output : Perfect Number
def CheckPerfect(Value):
    Sum=0
    for i in range(1,Value):
        if(Value%i==0):
            Sum=Sum+i
    if(Value==Sum):
        return True
    else:
        return False
        
def main():
    print("Enter the Number : ")
    No=int(input())
    
    Flag=CheckPerfect(No)
    if(Flag==True):
        print("Perfect Number")
    else:
        print("Not Perfect Number")

if __name__=="__main__":
    main()