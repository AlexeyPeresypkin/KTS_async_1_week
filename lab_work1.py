import requests
import time
from threading import Thread
import multiprocessing


def sync_count_time(url, count=10):
    start_time = time.time()
    for _ in range(count):
        requests.get(url)
    end_time = time.time()
    return end_time - start_time


def thread_count_time(url, count=10):
    start_time = time.time()
    threads = [Thread(target=requests.get, args=(url, )) for _ in range(count)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time


def multi_count_time(url, count=10):
    start_time = time.time()
    with multiprocessing.Pool(count) as pool:
        results = []
        for _ in range(count):
            results.append(pool.apply_async(requests.get, args=(url, )))

        for result in results:
            result.get()
    end_time = time.time()
    return end_time - start_time


url = 'https://api.covidtracking.com/v1/us/current.json'
print(f'Время последовательных запросов {sync_count_time(url)}')
print(f'Время запросов в тредах {thread_count_time(url)}')
print(f'Время запросов в процессах {multi_count_time(url)}')
