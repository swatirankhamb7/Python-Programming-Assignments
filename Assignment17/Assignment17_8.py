'''WAP  which accept one number and display below pattern.
   Input:5
   Output: 
   1 
   1 2 
   1 2 3
   1 2 3 4 
   1 2 3 4 5 
'''
def DisplayPattern(n):
    j=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    
def main():
    print("Enter the Number : ")
    No=int(input())

    DisplayPattern(No)
    
 
if __name__=="__main__":
    main()