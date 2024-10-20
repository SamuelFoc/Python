import threading
import time

def print_numbers(thread_id):
    for i in range(5):
        time.sleep(1)
        print(f"Thread {thread_id}: {i}")

# Creating multiple threads
threads = []
for i in range(3):  # Creating 3 threads
    thread = threading.Thread(target=print_numbers, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished execution.")