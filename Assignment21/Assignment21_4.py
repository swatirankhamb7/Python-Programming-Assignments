"""
4.Design a Python application that creates two threads.
Thread 1 should compute the sum of elements from a list.
Thread 2 should compute the product of elements from the same list.
Return the results to the main thread and display them.

"""
import threading
import time

iCnt=0
obj=threading.Lock()

def Sum(Numbers):
    Sum=0
    for i in Numbers:
        Sum+=i
    print("Sum of Numbers is : ",Sum)

def Product(Numbers):
    Ans=1
    for i in Numbers:
        Ans*=i
    print("Product of Numbers is : ",Ans)

    
def main():
    data = [100000, 111789, 2000, 258, 105623, 134343, 2567462, 234764, 1341321, 9173186,5,7,11,1000000009,10003,100000000003,999999937]

    start_time = time.time()

    t1 = threading.Thread(target=Sum, args=(data,))
    t2 = threading.Thread(target=Product, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()
    print("Execution Time :", end_time - start_time)
    print("End of Application")

if __name__=="__main__":
    main()
