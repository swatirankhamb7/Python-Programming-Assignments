"""1. Design automation script which accept directory name and display checksum of all files.
Usage :
DirectoryChecksum.py "Demo"

Demo is name of directory.
"""
import sys
import hashlib
import os
def CalculateCheckSum(Filename):
    Fobj=open(Filename,"rb")

    hobj=hashlib.md5()
    CheckSum=0
    Buffer=Fobj.read(1024)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=Fobj.read(1024)
    
    Fobj.close()
    return hobj.hexdigest()
    

def DirectoryScroll(Directory):
    Ret=os.path.exists(Directory)
    if(Ret==False):
     print("There is no such Directory...!")
     return
    
    Ret=os.path.isdir(Directory)
    if(Ret==False):
        print("There is no such a Directory")
        return
    boarder="-"*80
    fobj=open("Program1_Report.log","w")
    fobj.write(boarder+"\n")
    fobj.write("---------------------------------Marvellous Script ----------------------------"+"\n")
    fobj.write(boarder+"\n")
    for FolderName,SubFolderName,FileName in os.walk(Directory):
        for Fname in FileName:
            Fname=os.path.join(FolderName,Fname)
            CheckSum=CalculateCheckSum(Fname)
            fobj.write(f"File name : {Fname} "+"\n")
            fobj.write(f"CheckSum : {CheckSum}"+"\n")
            fobj.write("\n")

    fobj.write(boarder+"\n")
    fobj.write(boarder+"\n")
    print("Sucessfully Log File Created Check your Current Directory .......!")


def main():
    if(len(sys.argv)!=2):
        print('Usage :  DirectoryChecksum.py "Demo" ')
        print("Demo is name of directory.")
    else:
        DirectoryScroll(sys.argv[1])
if __name__=="__main__":
    main()