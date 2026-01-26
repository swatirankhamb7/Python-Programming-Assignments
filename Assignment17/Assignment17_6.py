'''WAP  which accept one number and display below pattern.
   Input:5
   Output: 
   *  *  *  *  *
   *  *  *  *
   *  *  *
   *  *
   *  
'''
def DisplayPattern(n):

    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
    
def main():
    print("Enter the Number : ")
    No=int(input())
    print()

    DisplayPattern(No)
     
if __name__=="__main__":
    main()