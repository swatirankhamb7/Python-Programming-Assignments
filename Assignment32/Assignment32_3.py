"""
3. Design automation script which accept directory name and delete all duplicate files from that directory.
 Write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be
 created into current directory.

Usage :
DirectoryDuplicateRemoval.py "Demo"

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
    

def FindDuplicate(Directory):
    Ret=os.path.exists(Directory)
    if(Ret==False):
     print("There is no such Directory...!")
     return
    
    Ret=os.path.isdir(Directory)
    if(Ret==False):
        print("There is no such a Directory")
        return
    boarder="-"*80
    fobj=open("log.txt","w")
    fobj.write(boarder+"\n")
    fobj.write("---------------------------------Marvellous Script ----------------------------"+"\n")
    fobj.write(boarder+"\n")
    Duplicates={}
    FileCount=0
    Cnt=0
    for FolderName,SubFolderName,FileName in os.walk(Directory):
        for Fname in FileName:
            FileCount+=1
            Fname=os.path.join(FolderName,Fname)
            CheckSum=CalculateCheckSum(Fname)
            if CheckSum in Duplicates:
                 Duplicates[CheckSum].append(Fname)
                 fobj.write(Fname+"\n")
                 Cnt+=1
            else:
               Duplicates[CheckSum] = [Fname]

            

    fobj.write(boarder+"\n")
    fobj.write(f"Total Files are : {FileCount}"+"\n")
    fobj.write(f"Total Duplicate Files are : {Cnt}"+"\n")
    fobj.write(f"Total Files Deleteted : {Cnt}"+"\n")
    fobj.write(boarder+"\n")
    print("Sucessfully Log File Created Check your Current Directory .......!")
    return Duplicates


def DeleteDuplicate(path="Automation"):
    MyDict = FindDuplicate(path)
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                os.remove(subvalue)
            

def main():
    if(len(sys.argv)!=2):
        print('Usage :  DirectoryChecksum.py "Demo" ')
        print("Demo is name of directory.")
    else:
        DeleteDuplicate(sys.argv[1])
if __name__=="__main__":
    main()