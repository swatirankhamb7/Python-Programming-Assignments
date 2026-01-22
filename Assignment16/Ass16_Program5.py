"""WAP which displays 10 to 1 on Screen.
Output : 10 9 8 7 6 5 4 3 2 1
"""

def DisplayNumbers(no):
    for i in range(no,0,-1):
        print(i,end="   ")
    
def main():
    print("Enter the Number : ")#10
    no=int(input())
    print()

    DisplayNumbers(no)

if __name__=="__main__":
    main()