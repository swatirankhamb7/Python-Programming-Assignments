"""WAP which  Display first 10 even numbers on Screen.
   Input: 2 4 6 8 10 12 14 16 18 20
"""

def Patterneven(no):
    for i in range(2,no*2+1,2):
        print(i,end="   ")
   
def main():
   Patterneven(10)
    
if __name__=="__main__":
    main()