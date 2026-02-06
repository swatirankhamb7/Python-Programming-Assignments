
"""2. Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extension.

Usage : DirectoryRename.py “Demo” “.txt” “.doc”

Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
After execution this script each .txt file gets renamed as .doc.
"""
import sys
import os
def ShowFile(Directory,Extension,Extension2):
    boarder="-"*80
    Ret=os.path.exists(Directory)
    if(Ret==False):
     print("There is no such Directory...!")
     return
    
    Ret=os.path.isdir(Directory)
    if(Ret==False):
        print("There is no such a Directory")
        return
    
    Filename="%sReport2.log"%(Directory)
    fobj=open(Filename,"w")
    fobj.write(boarder+"\n")
    fobj.write("---------------------------------Marvellous Script ----------------------------"+"\n")
    fobj.write(boarder+"\n")
    FileCount=0
    Cnt=0
    for Folder,SubFolder,Filename in os.walk(Directory):
        for Fname in Filename:
                  FileCount+=1
                  if Fname.endswith(Extension):
                   Fname=Fname.replace(Extension,Extension2)
                   fobj.write(Fname+"\n")
                   Cnt+=1

    fobj.write(boarder+"\n")
    fobj.write("Total File Scanned: "+str(FileCount)+"\n")
    fobj.write(f"{Extension} File Count : "+str(Cnt)+"\n")
    fobj.write(boarder+"\n")
        


def main():
    if(len(sys.argv)!=4):
        print('Usage : DirectoryRename.py “Demo” “.txt” “.doc”')
        print("Demo is name of directory and .txt is the extension that we want to search and rename with .doc.After execution this script each .txt file gets renamed as .doc.")
    else:
        ShowFile(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__=="__main__":
    main()