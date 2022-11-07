import os
import threading
import time

import requests
from dotenv import load_dotenv

load_dotenv()

prod_url = os.environ.get("TEST_URL")
email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
num_threads = 300

GENERATE_JWT_URL = f"{prod_url}/auth/generate-jwt-token/{email}"
FETCH_USER_URL = f"{prod_url}/user/{email}"

login_response = requests.post(GENERATE_JWT_URL)
jwt_token = login_response.json()["token"]


def worker(num):
    print("Thread ", num)
    resp = requests.get(
        FETCH_USER_URL,
        headers={"Authorization": f"Bearer {jwt_token}", "login-method": "HOSTED"},
    )
    print("Thread ", num, resp.json())


print("Starting timer...")
start_time = time.time()

threads = []
for i in range(num_threads):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print("joining %s", t.name)
    t.join()

time_taken = time.time() - start_time
print("Stopping timer...")
print("Number of threads: " + str(num_threads))
print("Execution time " + str(time_taken) + " seconds.\n")
