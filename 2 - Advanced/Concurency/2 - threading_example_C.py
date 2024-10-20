import threading

# Shared resource
counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        with lock:  # Acquiring the lock
            print(counter)
            counter += 1  # Critical section

# Creating multiple threads
threads = []
for _ in range(5):  # Creating 5 threads
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
