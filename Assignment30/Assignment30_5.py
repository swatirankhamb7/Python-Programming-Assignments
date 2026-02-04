"""
Q5) Search a Word in File
Problem Statement:
Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

Input:
Demo.txt Marvellous

Expected Output:
Display whether the word Marvellous is found in Demo.txt or not.
"""
import os
def main():
    Filename=input("Enter The File Name : ")

    Ret=os.path.exists(Filename)
    if(Ret==True):
     fobj=open(Filename,"r")
     Data=fobj.read()
     line_list=Data.split()
     word=input("Enter the String which you want to check in the given Data : ")

     Flag=False
     for i in line_list:
        if(i==word):
           Flag=True
    
     if(Flag==True):
       print("Given Word is present in File")
     else:
       print("Given Word is not Present in the File")

     
    else:
       print(f"{Filename} File Dont Exist")

if __name__=="__main__":
    main()