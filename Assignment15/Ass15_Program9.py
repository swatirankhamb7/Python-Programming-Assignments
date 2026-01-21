#Write a lambda function using reduce() which accepts list of numbers and returns Product of elements.
from functools import reduce
Product=lambda A,B:A*B
def main():
    data=list()
    print("Enter How many elements you want in list : ")
    num_elements=int(input())
    print("Enter the Elements: ")
    element=0
    for i in range(num_elements):
        element=int(input())
        data.append(element)
    print("Data  : ",data)

    result=reduce(Product,data)
    print("Product  is : ",result)
 
        
if __name__=="__main__":
    main()
    