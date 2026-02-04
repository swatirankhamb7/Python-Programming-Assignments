
"""
Q3) Copy File Contents into a New File (Command Line)
Problem Statement:
Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.

Input (Command Line):
ABC.txt

Expected Output:
Create Demo.txt and copy contents of ABC.txt into Demo.txt.
"""

import os
def main():
    FileName=input("Enter the File Name : ")
    FileName2=input("Enter the File Name which you want to create and write data in it: ")

    Ret=os.path.exists(FileName)
    if(Ret==True):
        fobj=open(FileName,"r")
        data=fobj.read()
        fobj2=open(FileName2,"w")
        fobj2.write(data)
        print("File Sucessfully Created and Data witten in it Sucessfully !")
    else:
        print(f"{FileName} not exists ")

if __name__=="__main__":
    main()
