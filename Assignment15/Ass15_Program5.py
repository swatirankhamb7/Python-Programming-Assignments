#Write a lambda function using reduce() which accepts list of numbers and returns maximum element.
from functools import reduce
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

    result=reduce((lambda X,Y:X if X>Y else Y ),data)
    print("Maximum is : ",result)
 
        
if __name__=="__main__":
    main()
    