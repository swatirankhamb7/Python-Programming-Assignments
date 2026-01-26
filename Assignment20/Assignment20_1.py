'''1: Design a Python application that creates two separate threads named Even and Odd.
The Even thread should display the first 10 even numbers.
The Odd thread should display the first 10 odd numbers.
Both threads should execute independently using the threading module.
Ensure proper thread creation and execution.'''

import threading
import time

def Even():
    for i in range(2,41,2):
        print("Inside Even : ",i)

def Odd():
    for i in range(1,40,2):
        print("Inside Odd : ",i)

def main():
    t1=threading.Thread(target=Even)
    t2=threading.Thread(target=Odd)
    start_time=time.time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_time=time.time()

    print("Execution time : ",start_time-end_time)

if __name__=="__main__":
    main()
