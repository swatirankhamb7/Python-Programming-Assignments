#Write a lambda function using map() which accepts list of numbers and returns a list of Squares of each number.

def main():
    data=list()
    print("Enter How many elements you want in list : ")
    Num_ele=int(input())
    print("Enter the Elements : ")
    element=0
    for i in range(Num_ele):
        element=int(input())
        data.append(element)
    print(data)
    Result=list()
    Result=list(map((lambda no:no**2),data))
    print(Result)

if __name__=="__main__":
    main()