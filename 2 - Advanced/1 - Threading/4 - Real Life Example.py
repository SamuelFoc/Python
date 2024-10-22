import threading
import time
import random

# Create a Semaphore with a limit of 2 to control access to coffee machines
coffee_machines = threading.Semaphore(2)

def customer(id: int):
    print(f"Customer {id} is trying to get coffee.")
    with coffee_machines:
        print(f"Customer {id} is using a coffee machine.")
        time_to_get_coffee = random.uniform(1, 3)
        time.sleep(time_to_get_coffee)
        print(f"Customer {id} is done getting coffee.")
    print(f"Customer {id} has finished and left the coffee machine.")

num_customers = 10
threads = [] 

# Create and start threads for each customer
for i in range(num_customers):
    thread = threading.Thread(target=customer, args=[i + 1])  # Create a thread for each customer
    threads.append(thread)  # Add the thread to the list
    thread.start()  # Start the thread

# Wait for all threads to finish
for thread in threads:
    thread.join()  # Ensure the main program waits for each customer to finish

# Print a final message after all customers have been served
print(f"All customers have been served!")