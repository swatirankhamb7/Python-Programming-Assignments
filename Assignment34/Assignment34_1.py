"""
Please add below features in our project named as Marvellous Data Shield System
1. Logging System
Create a Logs / folder
Store:
Backup start time
Files copied
Zip file name
Errors (if any)

2. Email Notification
Send an email after backup completion
Attach:
Log file
Zip file name

3. Restore Feature
Add a command:
python Script.py --restore ZipFileName Destination
Extract backup to given directory

4. Exclude Files / Folders

Ignore:
.tmp, .log, .exe
or user Defined Extension

5. Backup History Tracker
Maintain a file:
Date
Number of files
Zip size

Display history using:
python Script.py --history


"""
#CommandLine Input
import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

def make_zip(folder):
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name=folder+"_"+timestamp+".zip"
    #Open the zip file
                                      #Macros for Compress
    zobj=zipfile.ZipFile(zip_name,"w",zipfile.ZIP_DEFLATED)

    for root,dirs,files in os.walk(folder):
        for file in files:
            full_path=os.path.join(root,file)
            relative=os.path.relpath(full_path,folder)
            zobj.write(full_path,relative)
    zobj.close()
    return  zip_name


def calculate_hash(path):
    hobj=hashlib.md5()
    fobj=open(path,"rb")

    while True:
        data=fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    fobj.close
    return hobj.hexdigest()


def BackupFiles(Source,Destination):
    copied_Files=[]
    print("Creating Backup Folder for Backup Process : ")
    os.makedirs(Destination,exist_ok=True)#Nesting Level Folder Exist Ok by Dafault False
    for root,dirs,files in os.walk(Source):
        for file in files:
            src_path=os.path.join(root,file)

            relative=os.path.relpath(src_path,Source) 
            dest_path=os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            #Copy the Files if its New(os->Dirty read)
            if((not os.path.exists(dest_path)) or (calculate_hash(src_path)!=calculate_hash(dest_path))):
                shutil.copy2(src_path,dest_path) #CopyFile  with MetaData
                copied_Files.append(relative)
    return copied_Files




def  MarvellousDataSheildStart(Source="Data"):
    BackupName="MarvellousBackup"
    start_time=time.ctime()
    print("Backup Peocess Started Sucessfully At : ",time.ctime())
    files=BackupFiles(Source,BackupName)
    zip_files=make_zip(BackupName)
    print("Backup Completed Sucessfully ")

    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    Log_name="Marvellous"+"_"+timestamp+".log"
    fobj=open(Log_name,"a")
    boarder="_"*80
    fobj.write(boarder+"\n")
    fobj.write("---------------Marvellous data Shield System Log Report--------------"+"\n")
    fobj.write(boarder+"\n")
    fobj.write(f"Backup start time : {start_time}"+"\n")
    fobj.write(f"Files Copied : {len(files)}"+"\n")
    fobj.write(f"Zip files get created : {zip_files}"+"\n")
    fobj.write(boarder+"\n")
    fobj.close()
    print("Log Created Sucessfully......")
    

def main():
    boarder="-"*68
    print(boarder)
    print("---------------Marvellous data Shield System--------------")
    print(boarder)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H" ):
            print("This script is used to : ")
            print("1.Takes Autobackup at Given Time")
            print("2.Backup only new and Updated Files")
            print("Create an archive of the backup periodically.")
            

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U" ):
            print("Usage : use Automation script as ")
            print("Script.py Timeinterval SourceDirectory")
            print("Timeinterval : time in minutes for periodic scheduling")
            print("SourceDirectory : Name of the directory to backed up")
            

        else:
            print("Unable to procced There is no such option")
            print("Please use --h or --u to get more details")
    
    #python Demo.py 5 Data
    elif(len(sys.argv)==3):
        print("Inside Project Logic")
        print("Time interval: ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])
        
        #Apply the Schedular
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataSheildStart,sys.argv[2])
        print("Data Sheild System started Sucessfully...!")
        
        print("Time Interval in Minutes : ",sys.argv[1])
        print("Press Ctrl+C to stop the Execution")

        #Wait till Abort
        while True:
            schedule.run_pending()
            time.sleep(1)


    else:
         print("Invalid No of CommandLine Arguments")
         print("Unable to procced There is no such option")
         print("Please use --h or --u to get more details")



    print(boarder)
    print("---------------------Thank you For Using Our System------------------")
    print(boarder)

    

if __name__=="__main__":
    main()