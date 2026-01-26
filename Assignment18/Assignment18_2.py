'''Write a program which accept N numbers from user and store it into List. Return Maximum number from thst
Input : Number of elements : 6
Input Elements : 13  5  45  7  4   56
Output : 56
'''
def MaximumofList(List,n):
    Max=0
    for i in range(n):
        if(List[i]>Max):
            Max=List[i]
    return Max

def main():
    no=int(input("Enter the no of Elements you want in list : "))
    List=[]
    Element=0
    print("Enter the Elements to add in the List : ")

    for i in range (no):
        Element=int(input())
        List.append(Element)
    print(List)
    
    Result=MaximumofList(List,no)
    print("Maximum among the list is : ",Result)

if __name__=="__main__":
    main()