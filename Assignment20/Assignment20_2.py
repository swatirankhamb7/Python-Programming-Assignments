'''2: Design a Python application that creates two threads named EvenFactor and OddFactor.
Both threads should accept one integer number as a parameter.

The EvenFactor thread should:
Identify all even factors of the given number.
Calculate and display the sum of even factors.

The OddFactor thread should:
Identify all odd factors of the given number.
Calculate and display the sum of odd factors.

After both threads complete execution, the main thread should display the message:
“Exit from main”.'''

import threading
import time

def EvenFactor(no):
    Sum=0
    for i in range(2,int(no/2)+1,2):
        if(no%i==0):
         print("Inside EvenFactor : ",i)
         Sum+=i

    print("Sum of Even Factors : ",Sum)


def OddFactor(no):
    Sum=0
    for i in range(1,int(no/2)+1,2):
        if(no%i==0):
         print("Inside OddFactor : ",i)
         Sum+=i

    print("Sum of Odd Factors : ",Sum)

def main():
    t1=threading.Thread(target=EvenFactor,args=(10000,))
    t2=threading.Thread(target=OddFactor,args=(10000,))
    start_time=time.time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_time=time.time()

    print("Execution time : ",start_time-end_time)
    print("Exit from main")

if __name__=="__main__":
    main()
