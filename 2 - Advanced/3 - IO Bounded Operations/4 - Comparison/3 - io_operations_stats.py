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


iterations = [10, 100, 1000, 10000, 100000]
data = []
for iteration_num in iterations:
    print(f"Iterations: {iteration_num}")
    synchronous_time, threading_time, asyncio_time = cmp.compare_performance(iteration_num, workload, callback, ["data-tmp.txt"])
    data.append([synchronous_time, threading_time, asyncio_time])

# Prepare data for plotting
methods = ['Synchronous', 'Threading', 'Asyncio']

cmp.plot_data(data, iterations, methods)
