'''Write a program which accept N numbers from user and store it into List. Return addition of all elements
 from that List.
Input : Number of elements : 6
Input Elements : 13  5  45  7  4   56
Output : 130'''
def AddofList(List,n):
    Sum=0
    for i in range(n):
        Sum+=List[i]
    return Sum


def main():
    no=int(input("Enter the no of Elements you want in list : "))
    List=[]
    Element=0
    print("Enter the Elements to add in the List : ")

    for i in range (no):
        Element=int(input())
        List.append(Element)
    print(List)
    
    Result=AddofList(List,no)
    print("Addition of List Elements is : ",Result)
    
if __name__=="__main__":
    main()