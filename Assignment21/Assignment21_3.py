"""
3: Design a Python application where multiple threads update a shared variable.
Use a Lock to avoid race conditions.
Each thread should increment the shared counter multiple times.
Display the final value of the counter after all threads complete execution.
"""
import threading
import time

iCnt=0
obj=threading.Lock()

def Update():
    global iCnt
     
    for _ in range(2000000):
        with obj:
         iCnt+=1

    
def main():
    global iCnt
    t1=threading.Thread(target=Update)
    t2=threading.Thread(target=Update)
    start_time=time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time.time()
    print("Value of iCnt : ",iCnt)
    print("Execution Time : ",start_time-end_time)

    

if __name__=="__main__":
    main()
