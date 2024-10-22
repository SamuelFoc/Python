import threading
import time

# Create a Lock object to ensure that only one thread can print at a time
semaphore = threading.Semaphore(2)

def show_message(msg: str, delay: int = 1, id: int = -1):
    with semaphore:
        print(f"Started Thread: {id}")
        time.sleep(delay)
        print(msg)
        print(f"Ended Thread: {id}")

# Creating threads with the show_message function as the target.
thread_1 = threading.Thread(target=show_message, args=["My 1st thread!", 1, 1])
thread_2 = threading.Thread(target=show_message, args=["My 2nd thread!", 1, 2])
thread_3 = threading.Thread(target=show_message, args=["My 3rd thread!", 1, 3])
thread_4 = threading.Thread(target=show_message, args=["My 4th thread!", 1, 4])

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