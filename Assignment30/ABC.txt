"""
Q2) Count Words in a File
Problem Statement:
Write a program which accepts a file name from the user and counts the total number of words in that file.

Input:
Demo.txt

Expected Output:
Total number of words in Demo.txt.
"""
import os
def main():
    FileName=input("Enter the FileName : ")
    Ret=os.path.exists(FileName)

    if(Ret==True):
      fobj=open(FileName,"r")
      Data=fobj.read()
      Words=Data.split()
      Words_Count=len(Words)
      print("Count of Words is : ",Words_Count)

    else:
       print(f"{FileName} not Exists")

if __name__=="__main__":
    main()
