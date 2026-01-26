'''4: Design a Python application that creates three threads named Small, Capital, and Digits.
All threads should accept a string as input.
The Small thread should count and display the number of lowercase characters.
The Capital thread should count and display the number of uppercase characters.
The Digits thread should count and display the number of numeric digits.
Each thread must also display:
Thread ID
Thread Name
'''
import threading
import time

def Small(string):
    iCnt=0
    for i in string:
        if(i.islower()):
            iCnt+=1
    print("Thread Id : ",threading.current_thread().name)
    print("Thread Id : ",threading.get_ident())
    print("Small Count : ",iCnt)



def Capital(string):
    iCnt=0
    for i in string:
        if(i.isupper()):
            iCnt+=1
    print("Thread Id : ",threading.current_thread().name)
    print("Thread Id : ",threading.get_ident())
    print("Capital Count : ",iCnt)

def Digits(string):
    iCnt=0
    for i in string:
        if(i.isdigit()):
            iCnt+=1
    print("Thread Id : ",threading.current_thread().name)
    print("Thread Id : ",threading.get_ident())
    print("Digit Count : ",iCnt)

def main():
    string=input("Enter a string : ")
    t1=threading.Thread(target=Small,args=(string,))
    t2=threading.Thread(target=Capital,args=(string,))
    t3=threading.Thread(target=Digits,args=(string,))
    start_time=time.time()
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    end_time=time.time()

    print("Execution time : ",start_time-end_time)
    print("Exit from main")

if __name__=="__main__":
    main()
