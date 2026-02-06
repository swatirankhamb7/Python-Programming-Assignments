"""
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

"""
"""1. Design automation script which accept directory name and file extension from user. Display all files with that extension.
Usage : DirectoryFileSearch.py "Demo" ".txt"
Demo is name of directory and .txt is the extension that we want to search.
"""
import sys
import os
def ShowFile(Directory,Extension):
    boarder="-"*80
    Ret=os.path.exists(Directory)
    if(Ret==False):
     print("There is no such Directory...!")
     return
    
    Ret=os.path.isdir(Directory)
    if(Ret==False):
        print("There is no such a Directory")
        return
    
    Filename="%sReport.log"%(Directory)
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
                   fobj.write(Fname+"\n")
                   Cnt+=1

    fobj.write(boarder+"\n")
    fobj.write("Total File Scanned: "+str(FileCount)+"\n")
    fobj.write(f"{Extension} File Count : "+str(Cnt)+"\n")
    fobj.write(boarder+"\n")
        


def main():
    if(len(sys.argv)!=3):
        print('Usage :  DirectoryFileSearch.py "Demo" ".txt" ')
        print("Demo is name of directory and .txt is the extension that we want to search.")
    else:
        ShowFile(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()