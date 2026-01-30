class Numbers:
    def __init__(self,No):
        print("Inside Constructor ")
        self.Value=No
    
    def ChkPrime(self):
        for i in range(2,int(self.Value/2)):
            if(self.Value%i==0):
                return False
        return True
    
    def SumFactors(self):
        Sum=0
        for i in range(1,int((self.Value/2))+1):
            if(self.Value%i==0):
                Sum+=i
        return Sum

    
    def ChkPerfect(self):
        Sum=0
        Sum=self.SumFactors()
        if(Sum==self.Value):
            return True
        else:
            return False
    
    def Factors(self):
        print(f"Factors of {self.Value } is : ")
        for i in range(1,int((self.Value/2))+1):
            if(self.Value%i==0):
                print(i,end=" ")
        print()

    def Display(self):
        self.Factors()

        isPrime=self.ChkPrime()
        if(isPrime==True):
            print(self.Value,"is Prime Number")
        else:
            print(self.Value,"is not Prime Number")


        Sum=self.SumFactors()
        print(f"Sum of Factors of {self.Value} is : ",Sum)

        isPerfect=self.ChkPerfect()
        if(isPerfect==True):
            print(self.Value,"is Perfect Number")
        else:
            print(self.Value,"is not  Perfect Number")
        print()



obj1=Numbers(10)
obj1.Display()

obj1=Numbers(28)
obj1.Display()

obj1=Numbers(786)
obj1.Display()

obj1=Numbers(17)
obj1.Display()

obj1=Numbers(1)
obj1.Display()




        

        
  