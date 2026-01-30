class BookStore:
    
    No_of_Books=0

    def __init__(self,Name,Author):
        self.BookName=Name
        self.BookAuthor=Author
        BookStore.No_of_Books+=1
    
    def Display(self):
        print("Book : ",self.BookName)
        print("Author : ",self.BookAuthor)
        print("No of Books : ",BookStore.No_of_Books)

obj1=BookStore("Linux System programming ","Robert Love")
obj1.Display()

obj2=BookStore("C programming ","Dennis Ritchie")
obj2.Display()




    
