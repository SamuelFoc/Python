import time
import threading

# In the previous example, the execution was synchronous (line by line),
# meaning we had to wait for the first task to complete before starting the next one.
# This increased the overall execution time of the program.
# Ideally, we want to start the second task while still waiting for the first task to finish.
# By using threads, we can run these tasks concurrently, which will reduce the total execution time.

# Expensive function that simulates a 2-second I/O task
def expensive_io_task(message: str):
    time.sleep(2)
    print(message)

# --- EXECUTION MEASSUREMENT ---
start = time.perf_counter()

threads = []  # List to keep track of threads

# Pass the function and its arguments using 'target' and 'args'.
# Create the first thread for the first I/O task
thread_task_1 = threading.Thread(target=expensive_io_task, args=("First I/O task!",))
threads.append(thread_task_1)
thread_task_1.start()  # Start the first thread

# Create the second thread for the second I/O task
thread_task_2 = threading.Thread(target=expensive_io_task, args=("Second I/O task!",))
threads.append(thread_task_2)
thread_task_2.start()  # Start the second thread

# Wait for both threads to finish
for thread in threads:
    thread.join()

# After both tasks are complete, inform the user
print("Expensive tasks done!")

end = time.perf_counter()
# --- EXECUTION MEASSUREMENT ---

print(f"Execution Time: {round((end - start)*1000, 2)}ms")