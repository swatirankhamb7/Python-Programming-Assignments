'''
Write a program which contains filter(), map() and reduce() in it. Python application which contains
one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all 
such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase 
each number by 10. Reduce will return product of all that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000

'''
from functools import reduce

UpdatedData=lambda No:No>=70 and No<=90
Increment=lambda No:No+10
Product=lambda A,B:A*B

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
    fData=list(filter(UpdatedData,Arr))
    print("Data After Fileration : ",fData)

    #Map
    MData=list(map(Increment,fData))
    print("Data After Mapping : ",MData)

    #Reduce
    Result=reduce(Product,MData)
    print("Result : ",Result)

if __name__=="__main__":
    main()