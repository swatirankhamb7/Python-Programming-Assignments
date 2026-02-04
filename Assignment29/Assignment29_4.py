
"""
Q4) Compare Two Files (Command Line)

Problem Statement:
Write a program which accepts two file names through command line arguments and compares the contents of both files.
If both files contain the same contents, display Success
Otherwise display Failure

Input (Command Line):
Demo.txt Hello.txt

Expected Output:
Success OR Failure
"""

import sys
import os
def main():
    if(len(sys.argv)==3):
       FileName1=sys.argv[1]
       FileName2=sys.argv[2]
       Ret1=os.path.exists(FileName1)
       Ret2=os.path.exists(FileName2)

       if(Ret1==True and Ret2==True):
          fobj1=open(FileName1,"r")
          data1=fobj1.read()

          fobj2=open(FileName2,"r")
          data2=fobj2.read()

          if(data1==data2):
              print("Success.....!")

          else:
              print("Failure!")

       elif(Ret1==False and Ret2==True):
             print(f"{FileName1} not Exists")
            
        
       elif(Ret1==False and Ret2==False):
             print(f"{FileName1} and {FileName2} not Exists")
   
       else:
           print(f"{FileName2} not Exists")
           
             
    else:
        print("Enter the Three  Arguments like : Filename Demo.txt Hello.txt")

if __name__=="__main__":
    main()
