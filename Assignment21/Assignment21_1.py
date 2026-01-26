"""1: Design a Python application that creates two threads named Prime and NonPrime.
Both threads should accept a list of integers.
The Prime thread should display all prime numbers from the list.
The NonPrime thread should display all non-prime numbers from the list.
"""
import threading
import time

def Prime(numbers):
    for num in numbers:
        if num > 1:
            for i in range(2, int(num / 2) + 1):
                if num % i == 0:
                    break
            else:
                print("Prime no :", num)

def NonPrime(numbers):
    for num in numbers:
        if num <= 1:
            print("Non Prime no :", num)
        else:
            for i in range(2, int(num / 2) + 1):
                if num % i == 0:
                    print("Non Prime no :", num)
                    break

def main():
    data = [100000, 111789, 2000, 258, 105623, 134343, 2567462, 234764, 1341321, 9173186,5,7,11,1000000009,10003,100000000003,999999937]

    start_time = time.time()

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()
    print("Execution Time :", end_time - start_time)

if __name__ == "__main__":
    main()
