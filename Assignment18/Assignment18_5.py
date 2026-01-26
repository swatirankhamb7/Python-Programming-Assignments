'''
Write a program which accept N numbers from user and store it into List. Return addition of all 
prime numbers from that List. Main python file accepts N numbers from user and pass each number to 
ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function 
from main python file should be ListPrime().

Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 + 2 + 5)
'''
from MarvellousNum import CheckPrime,Addition
from functools import reduce

def main():
    no=int(input("Enter the no of Elements you want in list : "))
    Data=[]
    Element=0
    print("Enter the Elements to add in the List : ")

    for i in range (no):
        Element=int(input())
        Data.append(Element)
    print(Data)
    
    Prime_list=list(filter(CheckPrime,Data))
    print("Prime Numbers List Only : ",Prime_list)

    Result=reduce(Addition,Prime_list)
    print("Addition is : ",Result)
    
if __name__=="__main__":
    main()