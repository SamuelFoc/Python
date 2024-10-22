import math
import numpy as np
import matplotlib.pyplot as plt
import compare.utils as cmp

def workload():
    for _ in range(100):
        math.factorial(500)

iterations = [10, 100, 1000, 10000]
data = []
for iteration_num in iterations:
    print(f"Iterations: {iteration_num}")
    synchronous_time, threading_time, asyncio_time = cmp.compare_performance(iteration_num, workload)
    data.append([synchronous_time, threading_time, asyncio_time])

# Prepare data for plotting
methods = ['Synchronous', 'Threading', 'Asyncio']

cmp.plot_data(data, iterations, methods)