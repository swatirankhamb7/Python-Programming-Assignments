"""WAP which accept name from user and display length of its name
   Input : Marvellous   Output :10
"""

def CheckNameLength(Name):
    return len(Name)
    
def main():
   print("Enter the name to find the length : ")
   name=input()

   Result=CheckNameLength(name)
   print(name," Length is : ",Result)
 
if __name__=="__main__":
    main()