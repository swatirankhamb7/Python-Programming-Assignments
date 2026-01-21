#Write a lamda function which accepts one  number and returns True id Divisible by 5.
IsDivisibleBy5=lambda Value:Value%5==0

def main():
    print("Enter the number to check number is Divisible by 5 : ")
    Number=int(input())

    Result=IsDivisibleBy5(Number)
    if(Result==True):
        print(Number," is Divisible by 5")
    else:
        print(Number," is Not Divisible by 5")  
    
    
if __name__=="__main__":
    main()