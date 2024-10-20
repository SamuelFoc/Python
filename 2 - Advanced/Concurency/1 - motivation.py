from data_utils.data_handler import DataHandler
from data_utils.plot import plot_data

# Define test parameters
test_rows = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
execution_times = []

# TEST
dh = DataHandler()
for n_rows in test_rows:
    ex_t = dh.create_big_data(5, n_rows, "bigdata")
    execution_times.append(ex_t)
    dh.purge()

# Plotting the data
plot_data(test_rows, execution_times, "No Concurrency")