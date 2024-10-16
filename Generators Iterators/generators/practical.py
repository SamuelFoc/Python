import os

# This script creates a large text file with 100,000 lines of content 
# and then provides an interactive application that allows the user to 
# view the file line-by-line by pressing "enter". The user can also exit
# the application by typing 'exit'.

# To run the script:
# 1. Ensure you have Python installed on your machine.
# 2. Save this code to a file, e.g., `line_reader.py`.
# 3. Run the script in the terminal using: `python line_reader.py`.
# 4. Follow the on-screen instructions to view the file content or exit.

# Create a test large file with 100,000 lines.
# Each line contains the text "Iteration number: <i>", where i is the line number.


# Create a test large file
test_file_path = "test.txt"
with open(test_file_path, "w") as file:
    for i in range(100000):
        file.write(f"Iteration number: {i}\n")

# Create a generator that yields a line from the file
def read_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line

def app(file_path):
    generator = read_line(file_path)

    print("Press enter to see the next iteration. Type 'exit' to quit.")
    while True:
        user_input = input()
        if user_input.lower() == 'exit':
            break

        if user_input.lower() == '':
            try:
                line = next(generator)
                print(line.strip())
            except StopIteration:
                print("End of the file reached.")
                break

app(test_file_path)