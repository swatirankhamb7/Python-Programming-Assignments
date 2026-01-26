"""
2: Design a Python application that creates two threads.
Thread 1 should calculate and display the maximum element from a list.
Thread 2 should calculate and display the minimum element from the same list.
The list should be accepted from the user.
"""
import threading
import time

def Maximum(Numbers):
    Max=0
    for Num in Numbers:
        if(Num>Max):
            Max=Num
    print("Maximum is : ",Max)

    
    
def Minimum(Numbers):
    Min=Numbers[0]
    for Num in Numbers:
        if(Num<Min):
            Min=Num
    print("Minimum  is : ",Min)
    
                
        
def main():
    data=[100000,111789,2000,258,105623,134343,2567462,234764,1341321,9173186]
    start_time=time.time()
    t1=threading.Thread(target=Maximum,args=(data,))
    t2=threading.Thread(target=Minimum,args=(data,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time.time()
    print("Execution Time : ",start_time-end_time)

if __name__=="__main__":
    main()
