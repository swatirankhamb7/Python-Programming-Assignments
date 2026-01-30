class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumfarance=0.0

    def Accept(self):
        self.Radius=float(input("Enter the Radius Of Circle : "))
        
    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius**2
    
    def CalculateCicumference(self):
        self.Circumfarance=2*Circle.PI*self.Radius

    def Display(self):
        print("Radius : ",self.Radius)
        print("Area : ",self.Area)
        print("Circumfarance : ",self.Circumfarance)
        print()

obj1=Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCicumference()
obj1.Display()

obj2=Circle()
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCicumference()
obj2.Display()
    
obj3=Circle()
obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCicumference()
obj3.Display()