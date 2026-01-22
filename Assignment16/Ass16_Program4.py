"""WAP which displays 5 times Marvellous on Screen
Output: Marvellous
        Marvellous
        Marvellous
        Marvellous
        Marvellous
"""
def Display(String,no):
    for i in range(no):#loop  till n-1 and starts from 0
        print(String)
    
def main():
    print("Enter the  String : ")#Marvellous
    Str=input()

    print("Enter the no of times you want to print the given String : ")
    no=int(input())
    print()

    Display(Str,no)

if __name__=="__main__":
    main()