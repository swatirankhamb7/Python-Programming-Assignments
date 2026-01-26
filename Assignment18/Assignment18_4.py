'''Write a program which accept N numbers from user and store it into List. Accept one another number
from user and return the frequency of that number from the list.
Input : Number of elements : 11
Input Elements : 13  5  45  7   4  56 5 34 2 5 65
Element to search =5
Output : 5
'''
def FrequencyofNo(List,n,Value):
    freq=0
    for i in range(n):
     if(List[i]==Value):
        freq+=1
    return freq


def main():
    no=int(input("Enter the no of Elements you want in list : "))
    List=[]
    Element=0
    print("Enter the Elements to add in the List : ")

    for i in range (no):
        Element=int(input())
        List.append(Element)
    print(List)
    
    Value=int(input("Enter the numbre you want to search : "))
    Result=FrequencyofNo(List,no,Value)

    print("Frquency of ",Value,"is : ",Result)

if __name__=="__main__":
    main()