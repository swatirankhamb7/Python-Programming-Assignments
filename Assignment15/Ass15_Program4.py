#Write a lambda function using reduce() which accepts list of numbers and returns addittion of elements.
from functools import reduce
Add=lambda No,Sum:Sum+No
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

    r_Data=reduce(Add,data)
    print("Addittion is : ",r_Data)
 
        
if __name__=="__main__":
    main()
    