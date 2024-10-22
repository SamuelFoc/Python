import os
import time
import shutil
import threading

class THDataHandler:
    def __init__(self):
        # Get the absolute path of the current script's directory
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = None

    def write_file(self, fd: int, n_rows: int, base_path: str):
        # Write a specified number of rows to a file named data-{fd}.txt in the given base path
        file_path = os.path.join(base_path, f"data-{fd}.txt")
        with open(file_path, "w") as file:
            # Write n_rows of dummy data to the file
            for _ in range(n_rows):
                file.write(f"{_} - This is a big data dummy row\n")

    def create_big_data(self, n_files: int, n_rows: int, base_dir: str):
        # Create a specified number of files, each containing a specified number of rows of dummy data
        base_path = os.path.join(self.script_path, base_dir)
        self.base_dir = base_path  # Store the base directory path for later use (purge)
        start_time = time.perf_counter()  # Start the timer to measure execution time

        # Create the base directory if it doesn't already exist
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        threads = []
        # Generate the specified number of files using threads
        for file_id in range(n_files):
            # Create a thread to write to a file, passing the necessary arguments
            thread = threading.Thread(target=self.write_file, args=(file_id, n_rows, base_path))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()  # Ensure the main thread waits for each thread to complete

        end_time = time.perf_counter()  # End the timer
        exec_time_ms = (end_time - start_time) * 1000  # Calculate execution time in milliseconds
        print(f"Execution time: {round(exec_time_ms, 3)}ms")  # Print the execution time
        return exec_time_ms  # Return the execution time for potential further use

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