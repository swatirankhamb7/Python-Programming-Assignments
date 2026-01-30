class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0
    
    def Accept(self):
        self.Value1=int(input("Enter the first number : "))
        self.Value2=int(input("Enter the Second number : "))

    def Addition(self):
        return self.Value1+self.Value2
    
    def Substraction(self):
        return self.Value1-self.Value2
    
    def Multiplication(self):
        return (self.Value1)*(self.Value2)
    
    def Division(self):
        return self.Value1/self.Value2

obj=Arithmetic()
obj.Accept()
print("Addition is : ",obj.Addition())
print("Substraction is : ",obj.Substraction())  
print("Multiplication is : ",obj.Multiplication())
print("Division is : ",obj.Division())

obj2=Arithmetic()
obj2.Accept()
print("Addition is : ",obj2.Addition())
print("Substraction is : ",obj2.Substraction())  
print("Multiplication is : ",obj2.Multiplication())
print("Division is : ",obj2.Division())
