import threading
import time

def print_message():
    for _ in range(5):
        time.sleep(2)  # Simulating a time-consuming task
        print(f"Side thread execution: #{_}")

# Creating a thread
thread = threading.Thread(target=print_message)

# Starting the thread
thread.start()

# Main thread continues to run
for _ in range(5):
    time.sleep(1)
    print(f"Main thread execution: #{_}")

# Wait for the thread to finish
thread.join()

print("Thread has finished execution.")