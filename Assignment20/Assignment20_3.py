'''
3: Design a Python application that creates two threads named EvenList and OddList.
Both threads should accept a list of integers as input.

The EvenList thread should:
Extract all even elements from the list.
Calculate and display their sum.

The OddList thread should:
Extract all odd elements from the list.
Calculate and display their sum.
Threads should run concurrently.
'''
import threading
import time

def EvenList(Data):
    Sum=0
    for i in Data:
        if(i%2==0):
         Sum+=i

    print("Sum of Even Elements : ",Sum)

def OddList(Data):
    Sum=0
    for i in Data:
        if(i%2!=0):
         Sum+=i

    print("Sum of Odd Elements : ",Sum)

def main():
    data=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,100000,20000000,3000000,4000000,5000000,11111,22222,33333,44444,55555]
    t1=threading.Thread(target=EvenList,args=(data,))
    t2=threading.Thread(target=OddList,args=(data,))
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
