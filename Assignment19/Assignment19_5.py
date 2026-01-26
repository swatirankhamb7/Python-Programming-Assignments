'''
Write a program which contains filter(), map() and reduce() in it. Python application which contains 
one list of numbers. List contains the numbers which are accepted from user. Filter should filter out
 all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from 
 that numbers. (You can also use normal functions instead of lambda functions).
Input List = [2, 70, 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
'''
from functools import reduce

def CheckPrime(no):
    if no<2:
        return False
    for i in range(2,int((no/2)+1)):
        if(no%i==0):
            return False
    return True 

def Maximum(no):
    pass
    

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
    fData=list(filter(CheckPrime,Arr))
    print("Data After Fileration : ",fData)

    # #Map
    MData=list(map(lambda no:no*2,fData))
    print("Data After Mapping : ",MData)

    # #Reduce

    Result=reduce(lambda X,Y:X if X>Y else Y,MData)
    print("Result : ",Result)

if __name__=="__main__":
    main()