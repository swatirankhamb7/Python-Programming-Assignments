"""
Q1) Count Lines in a File

Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file.

Input:
Demo.txt

Expected Output:
Total number of lines in Demo.txt.
"""
import os
def main():
    Filename=input("Enter The File Name : ")

    Ret=os.path.exists(Filename)
    if(Ret==True):
     fobj=open(Filename,"r")
     Data=fobj.read()
     line_list=Data.split("\n")
     Cnt=len(line_list)

     print(f"Lines in {Filename} is : {Cnt}")

    else:
       print(f"{Filename} File Dont Exist")

if __name__=="__main__":
    main()