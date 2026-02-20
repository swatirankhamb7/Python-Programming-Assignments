"""4. Add Periodic Email Reporting Feature
Automatically send system report through email at regular intervals.
Email must contain:
• Log file attachment
• Summary of:
  o Total processes
  o Top CPU usage processes
  o Top Memory usage processes
  o Top Thread count processes
  o Top Open file processes
  
Usage
PlatformSurveillance.py "MarvellousLogs" "receiver@gmail.com" 10
Where:
• MarvellousLogs → log folder
• receiver@gmail.com → receiver mail
• 10 → interval in minutes

Expected Output in Log File

Each process entry should include:
Process Name
PID
CPU %
Memory (RSS)
Threads Count
Open Files Count
Timestamp
"""
import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

def send_email(Log_Name1,Log_Name2):
    sender_email = "rnaksh2026@gmail.com"
    app_password = "mmivifhmvqjjgzxk"
    receiver_email = sys.argv[3]
    subject = "Marvellous Backup Files and Reports"
    body = "Backup Log File and Zip File is Attached Below"

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    with open(Log_Name1, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='octet-stream',
            filename=Log_Name1
        )
    
    with open(Log_Name2, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='octet-stream',
            filename=Log_Name2
        )

    # Use SMTP_SSL properly (NO starttls here)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("Mail Sent Successfully!")

def CreateLog(FolderName):
    boarder="-"*68
    Ret=False
    Ret=os.path.exists(FolderName)
    if(Ret==True):
        Ret=os.path.isdir(FolderName)
        if(Ret==False):
            print("Unable to create Folder")
            return

    else:
        os.mkdir(FolderName)
        print("Directory For Log Files get Created Sucessfully ..!")

    timstamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName1=os.path.join(FolderName,"Marvellous_%s.log"%timstamp)
    print("Log File Created With Name : ",FileName1)
    fobj=open(FileName1,"w")
    fobj.write(boarder+"\n")
    fobj.write("---------------Marvellous platform Surveillance System--------------"+"\n")
    fobj.write("Log Created at :  "+time.ctime()+"\n")
    fobj.write(boarder+"\n\n")
    fobj.write("---------------------System Report--------------------------------"+"\n")
    fobj.write("Cpu Usage :%s %%  \n\n"%(psutil.cpu_percent()))# How many Cpu usage done
    mem=psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%"%mem.percent+"\n\n")
    fobj.write("Disk Usage Report: %s "%mem.percent+"\n")
    for part in psutil.disk_partitions():#SCAN Drives like C,E
        try:
            usage=psutil.disk_usage(part.mountpoint)#Jithe Mount Zalay tyacha naav
            fobj.write("%s -> %s %% used: \n"%(part.mountpoint,usage.percent))
        except:
            pass
    fobj.write("\n")
    net=psutil.net_io_counters()
    fobj.write("Nertwork Usage Report : \n")
    fobj.write("sent : %.2f MB\n"%(net.bytes_sent/(1024*1024)))
    fobj.write("Received : %.2f MB\n"%(net.bytes_recv/(1024*1024)))
    fobj.write(boarder+"\n")

    #Process Logic
    Data=Processscan()
    for info in Data:
        fobj.write("PID : %s\n"%info.get("pid"))
        fobj.write("name : %s\n"%info.get("name"))
        fobj.write("username : %s\n"%info.get("username"))
        fobj.write("status : %s\n"%info.get("status"))
        fobj.write("Thred_Count : %s \n"%info.get("Thred_Count"))
        fobj.write("file_count : %s \n"%info.get("File_Count"))
        fobj.write("start_time : %s\n"%info.get("create_time"))
        fobj.write("CPU %% : %.2f\n"%info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n"%info.get("memory_percent"))
        fobj.write(boarder+"\n")


    fobj.write("-------------------------End of Log File------------------------------"+"\n")
    fobj.write(boarder+"\n")

    
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName2="Top10Process_%s.log"%(timestamp)
    fobj2=open(FileName2,"w")

    Data.sort(key=lambda x:x["memory_percent"],reverse=True)
    for info in Data[:10]:
        fobj2.write("PID : %s\n"%info.get("pid"))
        fobj2.write("name : %s\n"%info.get("name"))
        fobj2.write("username : %s\n"%info.get("username"))
        fobj2.write("status : %s\n"%info.get("status"))
        fobj2.write("Thred_Count : %s \n"%info.get("Thred_Count"))
        fobj2.write("file_count : %s \n"%info.get("File_Count"))
        fobj2.write("start_time : %s\n"%info.get("create_time"))
        fobj2.write("CPU %% : %.2f\n"%info.get("cpu_percent"))
        fobj2.write("Memory %% : %.2f\n"%info.get("memory_percent"))
        fobj2.write(boarder+"\n")
    fobj2.close()
    print("Top 10 Processes Updated")
    send_email(FileName1,FileName2)
    
def Processscan():
    #print("Process Scan Report : ")  
    listprocess=[]

    #Warm up for CPU Percent:for CPU percent(to know the previous state to comapre with new satate)
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)
    for proc in psutil.process_iter(attrs=["pid","name","username","status","create_time"])  :#Proc by default is Dictionary
      try:
        try:
          info=proc.as_dict(attrs=["pid","name","username","status","create_time"])
          #Convert create_time
          info["create_time"]=time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(info["create_time"]))

        except:
            info["create_time"]="NA"
         
        info["cpu_percent"]=proc.cpu_percent(None)
        info["memory_percent"]=proc.memory_percent()
        thread_count = proc.num_threads()
        info["Thred_Count"]=thread_count
        try:
                open_files = proc.open_files()
                file_count = len(open_files) if open_files else 0
        except (psutil.NoSuchProcess, psutil.AccessDenied):
                file_count = 0

        info["File_Count"]=file_count


        listprocess.append(info)
      except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
          pass
    return listprocess

    


def main():
    boarder="-"*68
    print(boarder)
    print("---------------Marvellous platform Surveillance System--------------")
    print(boarder)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H" ):
            print("This script is used to : ")
            print("1.Create Automatic logs")
            print("2:Executes perodically")
            print("3:Sends mail with the log")
            print("4:Store Information about Processes")
            print("5:Store Information about CPU")
            print("6.Store Information about RAM usage")
            print("7.Store Information About Secondary Storage")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U" ):
            print("Usage : use Automation script as ")
            print("Script.py Timeinterval DirectoryName")
            print("Timeinterval : time in minutes for periodic scheduling")
            print("DirectoryName: Name of Directory to scheduling Logs")

        else:
            print("Unable to procced There is no such option")
            print("Please use --h or --u to get more details")
    
   
    elif(len(sys.argv)==4):
        print("Inside Project Logic")
        print("Time interval: ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])
        
        #Apply the Schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])
        print("Platform Survellance System started Sucessfully...!")
        print("Directory Created With Name : ",sys.argv[2])
        print("Time Interval in Minutes : ",sys.argv[1])
        print("Receiver Email : ",sys.argv[3])
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