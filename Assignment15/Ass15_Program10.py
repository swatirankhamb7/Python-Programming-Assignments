#Write a lambda function using filer() which accepts list of numbers and returns the Contains only even numbers.

def main():
    data=list()
    print("Enter How many elements you want in list : ")
    num_elements=int(input())
    print("Enter the Elements: ")
    element=0
    for i in range(num_elements):
        element=int(input())
        data.append(element)
    print("Data Before Filteration : ",data)
 
    Count_Even=len(list(filter((lambda No:No%2==0),data)))
    print("Even Elements Count is : ",Count_Even)
        
if __name__=="__main__":
    main()