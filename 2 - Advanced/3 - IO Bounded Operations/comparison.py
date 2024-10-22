import os
import matplotlib.pyplot as plt

DATA_PATH = "data"

data = []
files = os.listdir(DATA_PATH)

for file in files:
    full_path = os.path.join(DATA_PATH, file)
    with open(full_path, "r") as data_file:
        lines = data_file.read().split("\n")
        lines = lines[1:]  # Skip header
        # Append data, ensuring we only include non-empty lines
        data.append([line.split(",") for line in lines if line])

# Assuming you have three files and want to access their data
sync_data = data[0]
conc_data = data[1]
async_data = data[2]

# Extract x and y data, converting y values to floats
sync_x_data = [sync[0] for sync in sync_data]
sync_y_data = [float(sync[1]) for sync in sync_data]  # Convert to float
conc_x_data = [conc[0] for conc in conc_data]
conc_y_data = [float(conc[1]) for conc in conc_data]  # Convert to float
async_x_data = [asyncs[0] for asyncs in async_data]
async_y_data = [float(asyncs[1]) for asyncs in async_data]  # Convert to float

# Plotting the data
plt.plot(sync_x_data, sync_y_data, label='Synchronous')
plt.plot(conc_x_data, conc_y_data, label='Concurrent')
plt.plot(async_x_data, async_y_data, label='Asynchronous')
plt.xlabel('X Data')  # Adjust as necessary
plt.ylabel('Y Data')  # Adjust as necessary
plt.yscale('log')
plt.title('Data Comparison')
plt.legend()  # Add a legend to identify lines
plt.show()