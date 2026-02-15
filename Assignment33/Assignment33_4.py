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
    FileName=os.path.join(FolderName,"Marvellous_%s.log"%timstamp)
    print("Log File Created With Name : ",FileName)
    fobj=open(FileName,"w")
    fobj.write(boarder+"\n")
    fobj.write("---------------Marvellous platform Surveillance System--------------"+"\n")
    fobj.write("Log Created at :  "+time.ctime()+"\n")
    fobj.write(boarder+"\n")
    fobj.write("\n \n  ")
    fobj.write("---------------------System Report--------------------------------"+"\n")
    fobj.write("Cpu Usage :%s %%  \n"%(psutil.cpu_percent()))# How many Cpu usage done
    fobj.write(boarder+"\n")
    mem=psutil.virtual_memory()
    fobj.write("RAM Usage : %s "%mem.percent)
    fobj.write(boarder+"\n")
    for part in psutil.disk_partitions():#SCAN Drives like C,E
        try:
            usage=psutil.disk_usage(part.mountpoint)#Jithe Mount Zalay tyacha naav
            fobj.write("%s->%s % used :"%(part.mountpoint),usage.percent)
            fobj.write(boarder+"\n")
        except:
            pass
    net=psutil.net_io_counters()
    fobj.write("Nertwork Usage Report\n")
    fobj.write("sent : %.2f MB\n"%(net.bytes_sent/(1024*1024))+"\n")
    fobj.write("Received : %.2f MB\n"%(net.bytes_recv/(1024*1024))+"\n")
    fobj.write(boarder+"\n")

    #Process Logic

    fobj.write("-------------------------End of Log File------------------------------"+"\n")
    fobj.write(boarder+"\n")

def Processscan():
    print("Process Scan Report : ")  

    for proc in psutil.process_iter(attrs=["pid","name","status"])  :
        info=proc.info
        print(info["pid"],info["name"],info["status"])

    


def main():
    Processscan()
    
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
    
    #python Demo.py 5 Marvellos
    elif(len(sys.argv)==3):
        print("Inside Project Logic")
        print("Time interval: ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])
        
        #Apply the Schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])
        print("Platform Survellance System started Sucessfully...!")
        print("Directory Created With Name : ",sys.argv[2])
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