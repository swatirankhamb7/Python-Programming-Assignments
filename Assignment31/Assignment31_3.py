
"""3. Design automation script which accept two directory names. Copy all files from first directory into second directory.
 Second directory should be created at run time.

Usage :DirectoryCopy.py "Demo" "Temp"

Demo is name of directory which is existing and contains files in it. We have to create new directory as Temp and copy all files from Demo to Temp.
"""
import sys
import os
import time

def ShowFile(Directory1,DirectoryCopy):
    boarder="-"*80
    Ret=os.path.exists(Directory1)
    if(Ret==False):
     print(f"{Directory1} There is no such Directory...!")
     return
    
    Ret=os.path.isdir(Directory1)
    if(Ret==False):
        print(f"{Directory1}There is no such a Directory")
        return
    
    Ret=os.path.isdir(DirectoryCopy)
    if(Ret==True):
        print(f"We can not create given {DirectoryCopy} Beacuse It Already Exist")
        print("Write Another Name to  Create the Directory")
        return
    

    os.mkdir(DirectoryCopy)
    robj=open("CopyReport.txt","w")
    robj.write(boarder+"\n")
    robj.write("---------------------------------Marvellous Script ----------------------------"+"\n")
    robj.write(boarder+"\n")
    Cnt=0
    for Folder,SubFolder,Filename in os.walk(Directory1):
        for Fname in Filename:
                  FilePath=None
                  DestPath=os.path.join(DirectoryCopy,Fname)
                  SrcPath = os.path.join(Folder, Fname)
                  fobj=open(SrcPath,"r")
                  fobjCopy=open(DestPath,"w")
                  fobjCopy.write(fobj.read())
                  robj.write(time.ctime()+"   "+Fname+"  "+"\n")
                  Cnt+=1
    
    robj.write(boarder+"\n")
    robj.write(f"These File are Sucessfully Copied from {Directory1} to {DirectoryCopy}"+"\n") 
    robj.write(f"Total File Copied : {Cnt}"+"\n")   
    robj.write(boarder+"\n")


def main():
    if(len(sys.argv)!=3):
        print('Usage :DirectoryCopy.py "Demo" "Temp"')
        print("Demo is name of directory which is existing and contains files in it. We have to create new directory as Temp and copy all files from Demo to Temp.")
    else:
        ShowFile(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()