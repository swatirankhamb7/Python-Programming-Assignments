#Write a lamda function using filter() which accepts list of Strings and returns having  length grater than 5
def main():
    data=list()
    print("Enter How many String you want to add in the list: ")
    num_elements=int(input())
    print("Enter the Elements: ")
    element=" "
    for i in range(num_elements):
        element=input()
        data.append(element)
    print("Data Before Filteration : ",data)
    Result=list(filter((lambda Str:len(Str)>5),data))
    print("Strings Having Length greater than 5 : ",Result)

    
 

if __name__=="__main__":
    main()