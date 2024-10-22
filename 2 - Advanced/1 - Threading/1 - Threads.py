import threading
import time

# To create and run a thread, you need to use the Thread class from the threading module.
# You pass a function to the Thread's target parameter.
# This can be done in several ways, such as directly passing the function name,
# using a lambda function, or by using the functools.partial for arguments.
def show_message(msg: str, delay: int = 1):
    time.sleep(delay)
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
# you will notice that the order in which the messages appear
# may vary. This is because threads run concurrently and
# the scheduling of threads is managed by the operating system,
# which can lead to different execution orders.