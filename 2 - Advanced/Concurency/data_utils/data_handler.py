import os
import time
import shutil

class DataHandler:
    def __init__(self):
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = None

    def create_big_data(self, n_files: int, n_rows: int, base_dir: str):
        base_path = os.path.join(self.script_path, base_dir)
        self.base_dir = base_path
        start_time = time.perf_counter()

        if not os.path.exists(base_path):
            os.makedirs(base_path)

        for file_id in range(n_files):
            file_path = os.path.join(base_path, f"data-{file_id}.txt")
            with open(file_path, "w") as file:
                for _ in range(n_rows):
                    file.write(f"{_} - This is a big data dummy row\n")
        
        end_time = time.perf_counter()
        exec_time_ms = (end_time - start_time)*1000 
        print(f"Execution time: {round(exec_time_ms, 3)}ms")
        return exec_time_ms


    def purge(self):
        path = self.base_dir
        if path and os.path.exists(path):
            try:
                shutil.rmtree(path)  # Remove the directory and all its contents
                print(f"Directory {path} and its contents have been deleted.")
            except Exception as e:
                print(f"Error occurred while deleting {path}: {e}")
        else:
            print(f"The directory {path} does not exist.")