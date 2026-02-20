"""


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
from datetime import date


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
    Cnt=0
    print("Creating Backup Folder for Backup Process : ")
    os.makedirs(Destination,exist_ok=True)#Nesting Level Folder Exist Ok by Dafault False
    for root,dirs,files in os.walk(Source):
        for file in files:
            Cnt+=1
            src_path=os.path.join(root,file)

            relative=os.path.relpath(src_path,Source) 
            dest_path=os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            #Copy the Files if its New(os->Dirty read)
            if((not os.path.exists(dest_path)) or (calculate_hash(src_path)!=calculate_hash(dest_path))):
                shutil.copy2(src_path,dest_path) #CopyFile  with MetaData
                copied_Files.append(relative)
    return copied_Files,Cnt

def send_email(Log_Name,Zip_Name):
    sender_email = "rnaksh2026@gmail.com"
    app_password = "mmivifhmvqjjgzxk"
    receiver_email = "rswati6301@gmail.com"
    subject = "Marvellous Backup Files and Reports"
    body = "Backup Log File and Zip File is Attached Below"

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    with open(Log_Name, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='octet-stream',
            filename=Log_Name
        )

   
    with open(Zip_Name, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='octet-stream',
            filename=Zip_Name
        )



    # Use SMTP_SSL properly (NO starttls here)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("Mail Sent Successfully!")


def  MarvellousDataSheildStart(Source="Data"):
    BackupName="MarvellousBackup"
    start_time=time.ctime()
    print("Backup Peocess Started Sucessfully At : ",time.ctime())
    files,Cnt=BackupFiles(Source,BackupName)
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
    end_time=time.ctime()
    #send_email(Log_name,zip_files)

    updateHistory(zip_files,Cnt,end_time)

def Restore(Source,Destination):
    if not os.path.isdir(Destination):
        os.makedirs(Destination,exist_ok=True)
    
    Abs_Path=os.path.abspath(Destination)

    try: 
        shutil.unpack_archive(Source,Abs_Path)
        print(f"Files are Sucessfully Backed up in {Destination} Folder")
    except Exception as e:
        print(e)


def updateHistory(ZipFile,FileCount,Backup_time):
        fobj=open("BackupHistory.txt","w")
        fobj.write(f"Last Updated Date : {date.today()}"+"\n")
        fobj.write(f"Last Updated {Backup_time} "+"\n")
        fobj.write(f"Zip File Size : {os.path.getsize(ZipFile)}"+"\n")
        fobj.write(f"File Count is : {FileCount}"+"\n")
        fobj.close()
        print("History Updated")

    

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


        elif(sys.argv[1]=="--History" or sys.argv[1]=="--history" ):
           if os.path.exists("BackupHistory.txt"):
               fobj=open("BackupHistory.txt","r")
               Data=fobj.read()
               print(Data)
            

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


    elif(len(sys.argv)==4):
        if(sys.argv[1]=="--Restore" or sys.argv[1]=="--restore"):
            print("File Extracting Started : ")
            print("Zip File Name to Extract: ",sys.argv[2])
            print("Destination to Extract : ",sys.argv[3])
            Restore(sys.argv[2],sys.argv[3])
        
    else:
         print("Invalid No of CommandLine Arguments")
         print("Unable to procced There is no such option")
         print("Please use --h or --u to get more details")



    print(boarder)
    print("---------------------Thank you For Using Our System------------------")
    print(boarder)

    

if __name__=="__main__":
    main()