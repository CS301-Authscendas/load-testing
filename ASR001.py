import time
import requests
import os
import threading
from dotenv import load_dotenv

load_dotenv()

test_url = os.environ.get("TEST_URL")
numThreads = 1000

def worker(num):
    print("Thread ", num)
    resp = requests.get(test_url)
    print("Thread ", num, resp)
    
print("Starting timer...")
start_time = time.time()

threads = []
for i in range(numThreads):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print('joining %s', t.name)
    t.join()

time_taken = time.time() - start_time
print("Stopping timer...")
print("Number of threads: " + str(numThreads))
print("Execution time " + str(time_taken) + " seconds.\n")
