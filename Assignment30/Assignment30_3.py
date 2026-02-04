"""
Q3) Display File Line by Line

Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

Input:
Demo.txt

Expected Output:
Display each line of Demo.txt one by one.

"""

import os
def main():
    FileName=input("Enter the FileName : ")
    Ret=os.path.exists(FileName)

    if(Ret==True):
      fobj=open(FileName,"r")
      Data=fobj.read()
      
      for line in Data:
         print(line,end="")

    else:
       print(f"{FileName} not Exists")

if __name__=="__main__":
    main()
