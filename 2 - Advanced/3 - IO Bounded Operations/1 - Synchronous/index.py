from sync_lib.data_handler import DataHandler
from sync_lib.plot import plot_data, save_to_file
import time

#! TO READ
# In this loop, data is read synchronously for each size defined in test_rows.
# This means that for each iteration, the file is processed line by line.
# As the number of rows grows, the time complexity increases, leading to
# exponentially longer execution times for larger data sizes.
# The key inefficiency here is that synchronous processing means the program waits 
# for each read operation to complete before moving to the next step, preventing 
# any parallelization or overlapping of computation and I/O operations.
# 
# With larger files, this synchronous approach becomes increasingly problematic.
# I/O operations are relatively slow compared to in-memory operations, 
# and synchronous reads block any other potential tasks from being executed 
# while waiting for data to be read. This causes a significant bottleneck.
# 
# Since the time taken to read the data grows disproportionately with the file size,
# we observe that the execution time grows exponentially with the size of the data, 
# as the file system and I/O bandwidth limitations become more apparent at larger scales.

# Define test parameters
num_of_files = 5
num_of_rows_in_file = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
execution_times = []

# TEST
dh = DataHandler()
start = time.perf_counter()
for n_rows in num_of_rows_in_file:
    execution_time = dh.create_big_data(5, n_rows, "bigdata")  # Synchronous data creation
    execution_times.append(execution_time)
    dh.purge()
end = time.perf_counter()

# Plotting the data
plot_data(num_of_rows_in_file, execution_times, "No Concurrency")

save_to_file("sync_times.txt", columns=[num_of_rows_in_file, execution_times], header=["Rows In File", "Execution Times [ms]"])

print(f"Execution Time: {round((end - start)*1000, 3)}ms")
#! Saved file will be inside the sync_lib module