
"""
Q1) Check File Exists in Current Directory
Problem Statement:Write a program which accepts a file name from the user and checks whether that file exists
 in the current directory or not.

Input:
Demo.txt

Expected Output:
Display whether Demo.txt exists or not.
"""

import os
def main():
    FileName=input("Enter the File Name which you want check whether is exists or not : ")

    Ret=os.path.exists(FileName)
    if(Ret==True):
        print(f"{FileName} exists")
    else:
        print(f"{FileName} not exists")

if __name__=="__main__":
    main()
