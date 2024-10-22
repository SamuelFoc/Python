import time
import matplotlib.pyplot as plt
import compare.utils as cmp

# Define the workload function
def workload():
    time.sleep(0.1)  # Simulate some work with a sleep of 0.1 seconds

# Number of iterations
n = 100

# Run the performance comparison
synchronous_time, threading_time, asyncio_time = cmp.compare_performance(n, workload)

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
