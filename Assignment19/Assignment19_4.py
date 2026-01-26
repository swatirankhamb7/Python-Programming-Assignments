'''
Write a program which contains filter(), map() and reduce() in it. Python application which contains one
 list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such 
 numbers which are even. Map function will calculate its square. Reduce will return addition of all that 
 numbers.

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
'''
from functools import reduce

EvenCheck=lambda No:No>=No%2==0
Square=lambda No:No**2
Addition=lambda A,B:A+B

def main():
    no=int(input("Enter the no of elements you want in list : "))
    print("Enter the Elements : ")
    element=0
    Arr=[]
    for i in range(no):
        element=int(input())
        Arr.append(element)
    
    print("Dataset : ",Arr)

    #Filter
    fData=list(filter(EvenCheck,Arr))
    print("Data After Fileration : ",fData)

    #Map
    MData=list(map(Square,fData))
    print("Data After Mapping : ",MData)

    #Reduce
    Result=reduce(Addition,MData)
    print("Result : ",Result)

if __name__=="__main__":
    main()