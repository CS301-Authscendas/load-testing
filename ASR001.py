import time

print("Starting timer...")
start_time = time.time()
time.sleep(10)
time_taken = time.time() - start_time
print("Stopping timer...")
print("Execution time " + str(time_taken) + " seconds.\n")
