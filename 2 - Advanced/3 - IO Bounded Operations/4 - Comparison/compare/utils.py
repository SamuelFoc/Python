import time
import threading
import asyncio
import matplotlib.pyplot as plt
import numpy as np

# 1. Synchronous version
def run_synchronous(n, workload):
    start_time = time.time()
    for _ in range(n):
        workload()
    return time.time() - start_time

# 2. Threading version
def run_with_threading(n, workload):
    threads = []
    start_time = time.time()
    for _ in range(n):
        thread = threading.Thread(target=workload)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()  # Wait for all threads to complete
    return time.time() - start_time

# 3. Asyncio version
async def async_workload(workload):
    # Simulate an asynchronous I/O operation
    await asyncio.to_thread(workload)  # Use asyncio.to_thread for running the I/O workload

async def run_with_asyncio(n, workload):
    tasks = []
    start_time = time.time()
    for _ in range(n):
        tasks.append(async_workload(workload))
    
    await asyncio.gather(*tasks)  # Run all tasks concurrently
    return time.time() - start_time

# Main execution to compare performance
def compare_performance(n, workload, callback=None, args=None):
    sync_time = run_synchronous(n, workload)
    thread_time = run_with_threading(n, workload)
    
    # Run asyncio event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    async_time = loop.run_until_complete(run_with_asyncio(n, workload))
    
    if callback and args:
        callback(*args)
    return sync_time, thread_time, async_time

# PLOTTING
def plot_data(y_data, x_data, drill):
    data = np.array(y_data)  # Convert the data list to a numpy array for easy indexing

    # Plotting the execution times for each iteration
    x = np.arange(len(x_data))  # X-axis positions for the iterations
    bar_width = 0.2  # Width of each bar

    plt.figure(figsize=(12, 6))

    # Plot each method with an offset on the X-axis
    for i, method in enumerate(drill):
        plt.bar(x + i * bar_width, data[:, i], width=bar_width, label=method)

    # Labeling the plot
    plt.title('Execution Time Comparison Across Iterations and Methods')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Execution Time (seconds)')
    plt.xticks(x + bar_width, x_data)  # Setting iteration numbers as X-axis labels
    plt.legend()
    plt.grid(axis='y')
    plt.tight_layout()

    # Show the plot
    plt.show()