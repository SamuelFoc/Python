import time

# Let's create a function that simulates an expensive I/O task by sleeping for 2 seconds.
def expensive_io_task(message: str):
    time.sleep(2)  # Simulates a 2-second I/O operation
    print(message)


# --- EXECUTION MEASSUREMENT ---
start = time.perf_counter()
# Now imagine that in your code you need to complete two expensive I/O tasks.
# Both tasks take the same amount of time (2 seconds), and neither depends on the other.
# Despite this, the current implementation runs them synchronously, one after the other.
# As a result, the total execution time will be the sum of both tasks' execution times (4 seconds).
expensive_io_task("First I/O task!")
expensive_io_task("Second I/O task!")

# After both tasks are complete, the following message will be printed to inform the user.
# Notice that this approach is inefficient because we could run both I/O tasks concurrently,
# cutting the total execution time in half (2 seconds instead of 4), since the tasks are independent.
print("Expensive tasks done!")

end = time.perf_counter()
# --- EXECUTION MEASSUREMENT ---

print(f"Execution Time: {round((end - start)*1000, 2)}ms")