import os
import matplotlib.pyplot as plt
import compare.utils as cmp

def workload():
    # Generate the specified number of files
    file_path = "data-tmp.txt"
    with open(file_path, "w") as file:
        for _ in range(1000):
            file.write(f"{_} - This is a tmp data dummy row\n")

def callback(path):
    os.remove(path)

# Number of iterations
n = 1000

# Run the performance comparison
synchronous_time, threading_time, asyncio_time = cmp.compare_performance(n, workload, callback, ["data-tmp.txt"])

# Prepare data for plotting
methods = ['Synchronous', 'Threading', 'Asyncio']
times = [synchronous_time, threading_time, asyncio_time]

# Plotting the execution times
plt.figure(figsize=(10, 5))
plt.bar(methods, times, color=['blue', 'orange', 'green'])
plt.title('Execution Time Comparison of Different Approaches')
plt.xlabel('Method')
plt.ylabel('Execution Time (seconds)')
plt.grid(axis='y')
plt.show()

synchronous_time, threading_time, asyncio_time
