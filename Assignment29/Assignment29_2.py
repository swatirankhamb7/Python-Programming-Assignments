
"""
Q2) Display File Contents
Problem Statement:
Write a program which accepts a file name from the user, opens that file, and displays the entire contents 
on the console.

Input:
Demo.txt

Expected Output:
Display contents of Demo.txt on console.

"""

import os
def main():
    FileName=input("Enter the File Name which you want to display its contents on Console: ")

    Ret=os.path.exists(FileName)
    if(Ret==True):
        fobj=open(FileName,"r")
        data=fobj.read()
        print("File Data is : ",data)
    else:
        print(f"{FileName} not exists ")

if __name__=="__main__":
    main()
