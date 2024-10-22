from conc_lib.data_handler import THDataHandler
from conc_lib.plot import plot_data, save_to_file
import time

# Define test parameters
num_of_files = 5
num_of_rows_in_file = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
execution_times = []

# TEST
dh = THDataHandler()
start = time.perf_counter()
for n_rows in num_of_rows_in_file:
    ex_t = dh.create_big_data(5, n_rows, "bigdata")
    execution_times.append(ex_t)
    dh.purge()
end = time.perf_counter()

# Plotting the data
plot_data(num_of_rows_in_file, execution_times, "Concurrency")

save_to_file("conc_times.txt", columns=[num_of_rows_in_file, execution_times], header=["Rows In File", "Execution Times [ms]"])

print(f"Execution Time: {round((end - start)*1000, 3)}ms")
#! Saved file will be inside the conc_lib module