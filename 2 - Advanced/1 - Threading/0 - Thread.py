import threading
import time

# To create and run a thread you have to use Thread class
# You have to pass a function into the Thread.target so
# you can do it in several ways (direct function pass, using lambda, ..)
def show_message(msg: str):
    time.sleep(1)
    print(msg)

thread = threading.Thread(target=show_message, args=["My first thread!"])

# Now you have to start it
thread.start()
# Wait for it to complete
thread.join()