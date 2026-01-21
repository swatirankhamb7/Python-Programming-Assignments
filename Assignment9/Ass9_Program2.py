#WAP which contains one function chkGreater() that accepts two numbers and print the greater number.
#Input : 10 20
#Output : 20 is greater

def chkGreater(Value1,Value2):
    if(Value1>Value2):
        print(Value1,"is greater")
    else:
        print(Value2,"is greater")


def main():
    print("Enter the first no : ")
    No1=int(input())

    print("Enter the Second no : ")
    No2=int(input())
    chkGreater(No1,No2)

if __name__=="__main__":
    main()