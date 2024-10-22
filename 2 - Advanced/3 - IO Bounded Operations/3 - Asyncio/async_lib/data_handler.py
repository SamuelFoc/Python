import os
import shutil
import asyncio

class AsyncDataHandler:
    def __init__(self):
        # Get the absolute path of the current script's directory
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = None

    async def write_file(self, fd: int, n_rows: int, base_path: str):
        # Write a specified number of rows to a file named data-{fd}.txt in the given base path
        file_path = os.path.join(base_path, f"data-{fd}.txt")

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self._write_to_file, file_path, n_rows)
        
    def _write_to_file(self, file_path: str, n_rows: int):
        with open(file_path, "w") as file:
            # Write n_rows of dummy data to the file
            for _ in range(n_rows):
                file.write(f"{_} - This is a big data dummy row\n")

    async def create_big_data(self, n_files: int, n_rows: int, base_dir: str):
        # Create a specified number of files, each containing a specified number of rows of dummy data
        base_path = os.path.join(self.script_path, base_dir)
        self.base_dir = base_path  # Store the base directory path for later use (purge)

        # Create the base directory if it doesn't already exist
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        start_time = asyncio.get_event_loop().time()  # Start the timer to measure execution time

        tasks = []
        # Generate the specified number of files using threads
        for file_id in range(n_files):
            # Create a thread to write to a file, passing the necessary arguments
            task = asyncio.create_task(self.write_file(file_id, n_rows, base_path))
            tasks.append(task)

        # Wait for all threads to finish
        await asyncio.gather(*tasks)

        end_time = asyncio.get_event_loop().time()  # End the timer
        exec_time_ms = (end_time - start_time) * 1000  # Calculate execution time in milliseconds
        print(f"Execution time: {round(exec_time_ms, 3)}ms")  # Print the execution time
        return exec_time_ms  # Return the execution time for potential further use

    async def purge(self):
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