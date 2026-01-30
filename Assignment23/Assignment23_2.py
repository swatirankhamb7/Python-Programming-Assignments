class BankAccount:
    ROI=10.5

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount
        self.Interest=0
    
    def Deposit(self,Amount):
        self.Amount+=Amount
    
    def Withdraw(self,Amount):
        if(self.Amount>Amount):
         self.Amount-=Amount
        else:
            print("Insufficient Balance to Withdraw")

    def CalculateInterest(self):
        self.Interest=(self.Amount*BankAccount.ROI)

    
    def Display(self):
        print("Account holder Name : ",self.Name)
        print("Bank Balance : ",self.Amount)
        
obj1=BankAccount("Swati Rankhamb",75000)
obj1.Deposit(20000)
obj1.Withdraw(75000)
obj1.Display()

obj2=BankAccount("Namrata Rankhamb",100000)
obj2.Deposit(20000)
obj2.Withdraw(5000)
obj2.Display()




    
