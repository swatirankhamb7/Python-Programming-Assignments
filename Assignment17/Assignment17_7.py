'''WAP  which accept one number and display below pattern.
   Input:5
   Output: 
   1 2 3 4 5
   1 2 3 4 5
   1 2 3 4 5
   1 2 3 4 5 
'''
def DisplayPattern(n):
    for i in range(n):
        for j in range(1,n+1):
            print(j,end=" ")
        print()
    
def main():
    print("Enter the Number : ")
    No=int(input())

    DisplayPattern(No)
      
if __name__=="__main__":
    main()