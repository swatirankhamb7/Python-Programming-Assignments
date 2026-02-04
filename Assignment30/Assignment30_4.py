"""
Q4) Copy File Contents into Another File
Problem Statement:
Write a program which accepts two file names from the user.
First file is an existing file
Second file is a new file
Copy all contents from the first file into the second file.

Input:
ABC.txt Demo.txt

Expected Output:
Contents of ABC.txt copied into Demo.txt.
"""
import os
def main():
    FileName=input("Enter the File Name : ")
    FileName2=input("Enter the File Name in which you want copy the data: ")

    Ret=os.path.exists(FileName)
    Ret2=os.path.exists(FileName2)
    
    if(Ret==True and Ret2==True):
        fobj=open(FileName,"r")
        data=fobj.read()
        fobj2=open(FileName2,"w")
        fobj2.write(data)
        print(f"Data Sucessfully  Copied from {FileName} and Written Sucessfully in {FileName2}")

    elif(Ret==True and Ret2==False):
        print(f"{FileName2} not exists ")

    else:
        print(f"{FileName} not exists ")

if __name__=="__main__":
    main()