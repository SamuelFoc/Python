import threading
import time

# Create a Lock object to ensure that only one thread can print at a time
print_lock = threading.Lock()

def show_message(msg: str, delay: int = 1):
    time.sleep(delay)
    # Acquire the lock before printing to prevent other threads from printing at the same time
    with print_lock:
        print(msg)

# Creating threads with the show_message function as the target.
thread_1 = threading.Thread(target=show_message, args=["My 1st thread!"])
thread_2 = threading.Thread(target=show_message, args=["My 2nd thread!"])
thread_3 = threading.Thread(target=show_message, args=["My 3rd thread!"])
thread_4 = threading.Thread(target=show_message, args=["My 4th thread!"])

# Store all the thread objects in a list for easy management.
threads = [thread_1, thread_2, thread_3, thread_4]

# Start all threads.
for thread in threads:
    thread.start()

# Wait for all threads to complete.
for thread in threads:
    thread.join()

# After running this code, if you execute it multiple times,
# the order of printed messages may still vary, but each message
# will be printed completely before another thread can start printing.