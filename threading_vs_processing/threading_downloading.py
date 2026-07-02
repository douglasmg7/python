#!/usr/bin/python
from threading import Thread
from time import sleep, perf_counter

def fetch_data(api_url):
    print(f'Downloading from {api_url}...')
    sleep(2)    # Simulates network latency.

urls = ['UrlA', 'UrlB', 'UrlC']
threads = []

start_time = perf_counter()

for url in urls:
    t = Thread(target=fetch_data, args=(url,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

elapsed_time = perf_counter() - start_time
print(f'Elapsed time: {elapsed_time:.6f} seconds')
