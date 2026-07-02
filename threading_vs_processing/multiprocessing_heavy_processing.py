#!/usr/bin/python
from multiprocessing import Process
import os
from time import sleep, perf_counter

def compute_heavy_math(number):
    print(f'Processing {number} on Core Process PID {os.getpid()}')
    return sum(i*i for i in range(number))

if __name__ == "__main__":
    numbers = [5_000_000, 6_000_000, 7_000_000]
    processes = []

    start_time = perf_counter()

    for number in numbers:
        p = Process(target=compute_heavy_math, args=(number,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    elapsed_time = perf_counter() - start_time
    print(f'Elapsed time: {elapsed_time:.6f} seconds')
