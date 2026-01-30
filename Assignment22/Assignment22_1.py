class Demo:
    Value=10

    def __init__(self,A,B):
        self.no1=A
        self.no2=B
        print("Inside Constructor")
        print()
    
    def Fun(self):
        print("Inside Fun ")
        print("No1:",self.no1)
        print("No1:",self.no2)
        print()

    def Gun(self):
        print("Inside Gun ")
        print("No1:",self.no1)
        print("No1:",self.no2)
        print()

obj1=Demo(11,21)
obj2=Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()