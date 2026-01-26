'''Write a program which accept N numbers from user and store it into List. Return Minimum number from thst
Input : Number of elements : 4
Input Elements : 13  5  45  7  
Output : 5
'''
def MinimumofList(List,n):
    Min=List[0]
    for i in range(n):
        if(List[i]<Min):
            Min=List[i]
    return Min

def main():
    no=int(input("Enter the no of Elements you want in list : "))
    List=[]
    Element=0
    print("Enter the Elements to add in the List : ")

    for i in range (no):
        Element=int(input())
        List.append(Element)
    print(List)
    
    Result=MinimumofList(List,no)
    print("Minimum among the list is : ",Result)

if __name__=="__main__":
    main()