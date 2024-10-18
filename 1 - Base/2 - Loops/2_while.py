# Initialize a variable to keep track of the count
count = 0

# While loop: continues to run as long as the condition (count < 5) is true
while count < 5:
    # Print the current value of count
    print(f"Current count: {count}")
    
    # Increment count by 1 for the next iteration
    count += 1  # This ensures that the loop will eventually terminate

# After the while loop, print a message indicating completion
print("Loop has completed.")

# Another example: A while loop to find even numbers up to 10
number = 0  # Initialize a variable to start from 0

print("Even numbers up to 10:")
while number <= 10:  # Continue looping as long as number is less than or equal to 10
    if number % 2 == 0:  # Check if the number is even (divisible by 2)
        print(number)  # Print the even number
    number += 1  # Increment number by 1 for the next iteration

# ! You can also use "break" and "continue" keywords with while loop