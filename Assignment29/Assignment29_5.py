"""
Q5) Frequency of a String in File

Problem Statement:
Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

Input:
Demo.txt Marvellous

Expected Output:
Count how many times "Marvellous" appears in Demo.txt.
"""

import os
def main():
    FileName=input("Enter the File Name : ")
    String=input("Enter the string which you want check : ")

    Ret=os.path.exists(FileName)
    if(Ret==True):
        fobj=open(FileName,"r")
        data=fobj.read()
        Count=0

        #Using count Method :
        Count=data.count(String)
        
        print(f"Count of {String} in give file is : ",Count)

    else:
        print(f"{FileName} not exists")

if __name__=="__main__":
    main()