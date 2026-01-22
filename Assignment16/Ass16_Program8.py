"""WAP which accept number from user and print that number of "*" on Screen.
   Input: 5  Output : *  *  *  *  *
"""

def PatternPrint(no):
    for _ in range(no):
        print("*",end="   ")
  
def main():
    print("Enter the Number : ")
    no=int(input())
    print()
    PatternPrint(no)

if __name__=="__main__":
    main()