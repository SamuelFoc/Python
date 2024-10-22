import os
import time
import shutil

class DataHandler:
    def __init__(self):
        # Initialize the DataHandler instance
        # Get the path of the current script directory
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = None  # Initialize base_dir to None, to be set when creating data

    def create_big_data(self, n_files: int, n_rows: int, base_dir: str):
        # Create a specified number of files, each containing a specified number of rows of dummy data
        base_path = os.path.join(self.script_path, base_dir)  # Create the full path for the base directory
        self.base_dir = base_path  # Store the base directory path for later use
        start_time = time.perf_counter()  # Start the timer to measure execution time

        # Create the base directory if it doesn't already exist
        if not os.path.exists(base_path):
            os.makedirs(base_path)  # Create the directory

        # Generate the specified number of files
        for file_id in range(n_files):
            file_path = os.path.join(base_path, f"data-{file_id}.txt")  # Define the file path
            with open(file_path, "w") as file:  # Open the file for writing
                # Write the specified number of rows to the file
                for _ in range(n_rows):
                    file.write(f"{_} - This is a big data dummy row\n")  # Write a dummy row

        end_time = time.perf_counter()  # End the timer
        exec_time_ms = (end_time - start_time) * 1000  # Calculate execution time in milliseconds
        print(f"Execution time: {round(exec_time_ms, 3)}ms")  # Print the execution time
        return exec_time_ms  # Return the execution time for further use

    def purge(self):
        # Delete the base directory and all its contents
        path = self.base_dir  # Retrieve the path of the directory to delete
        if path and os.path.exists(path):  # Check if the path exists
            try:
                shutil.rmtree(path)  # Remove the directory and all its contents
                print(f"Directory {path} and its contents have been deleted.")  # Confirmation message
            except Exception as e:  # Catch any exceptions during deletion
                print(f"Error occurred while deleting {path}: {e}")  # Print error message
        else:
            print(f"The directory {path} does not exist.")  # Inform if the directory does not exist