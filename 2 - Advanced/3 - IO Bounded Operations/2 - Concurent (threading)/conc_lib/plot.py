import matplotlib.pyplot as plt
import os

def plot_data(x: list, y: list, title: str = "", save_path: str = None):
    plt.plot(x, y, marker='o')
    plt.xlabel('Number of Rows')
    plt.ylabel('Execution Time (ms)')
    plt.title(title)
    plt.xscale('log')
    # plt.yscale('log') # Uncomment for log scale on Y axis
    plt.grid(True)
    
    if save_path:  # If a save path is provided, save the figure
        plt.savefig(save_path)  # Save the figure to the specified path
        print(f"Plot saved as {save_path}")
    else:
        plt.show() 

def save_to_file(file_name: str, columns: list, header: list = None):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)
    
    column_lengths = [len(column) for column in columns]
    if max(column_lengths) != min(column_lengths):
        raise TypeError("All the columns must be of the same length!")

    try:
        with open(file_path, "w") as file:
            if header:
                header_str = ",".join(header)
                file.write(header_str + "\n")
            for row_idx in range(len(columns[0])):
                row_str = ",".join(str(column[row_idx]) for column in columns)
                file.write(row_str + "\n")
    except Exception as error:
        raise IOError(f"Error occured during write: {error}")

    print("File saved successfully!")