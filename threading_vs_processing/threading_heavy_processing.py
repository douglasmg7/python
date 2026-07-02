#!/usr/bin/python
from threading import Thread
from time import sleep, perf_counter

def compute_heavy_math(number):
    print(f'Processing {number}...')
    return sum(i*i for i in range(number))

numbers = [5_000_000, 6_000_000, 7_000_000]
threads = []

start_time = perf_counter()

for number in numbers:
    thread = Thread(target=compute_heavy_math, args=(number,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

elapsed_time = perf_counter() - start_time
print(f'Elapsed time: {elapsed_time:.6f} seconds')
