'''
5: Design a Python application that creates two threads named Thread1 and Thread2.
Thread1 should display numbers from 1 to 50.
Thread2 should display numbers from 50 to 1 in reverse order.
Ensure that:
Thread2 starts execution only after Thread1 has completed.
Use appropriate thread synchronization.
'''

import threading
import time

lobj=threading.Lock()

def Thread1():
    for i in range(1,51):
        with lobj:
         print(i)
        
def Thread2():
    for i in range(50,0,-1):
        print(i)
    

def main():
    t1=threading.Thread(target=Thread1)
    t2=threading.Thread(target=Thread2)
    start_time=time.time()
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    end_time=time.time()

    print("Execution time : ",start_time-end_time)
    print("Exit from main")

if __name__=="__main__":
    main()
