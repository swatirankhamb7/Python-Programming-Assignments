#WAP which accepts marks and Displays Grade.
#Condition Example
#>=75->Distinction
#>=60->First Class
#>=50->Second Class
#<50->
def Grade(Marks):
    if(Marks>100):
        print("Enter the Valid Marks")
    elif(Marks>=75):
        print("Distinction")
    elif(Marks>=60):
        print("First Class")
    elif(Marks>=59):
        print("Second Class")
    else:
        print("Fail")

def main():
    print("Enter the marks: ")
    Marks=int(input())
    Grade(Marks)

if __name__=="__main__":
    main()