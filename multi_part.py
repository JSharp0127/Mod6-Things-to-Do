"""Chapter 15 Things to do"""
import multiprocessing
import datetime
import random
import time

def current(num):
    print(f'The current time is {num}')

if __name__ == "__main__":
    for n in range (3):
        time.sleep(random.uniform(0,1))
        p= multiprocessing.Process(target=current, args=(datetime.datetime.now(),))
        p.start()
