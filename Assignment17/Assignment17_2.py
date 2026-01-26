'''WAP  which accept one number from user and display below Pattern.
   Input:5
   Output:
   *  *   *   *  *
   *  *   *   *  *
   *  *   *   *  *
   *  *   *   *  *
   *  *   *   *  *
'''
def DisplayPattern(n):
    for _ in range(n):
        for _ in range(n):
            print("*",end="  ")
        print()
    
def main():
    print("Enter the Number : ")
    No=int(input())
    DisplayPattern(No)
   
if __name__=="__main__":
    main()