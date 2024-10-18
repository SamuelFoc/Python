# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# List of temperatures in Celsius
celsius_temperatures = [0, 20, 37, 100]

# Use map to convert Celsius to Fahrenheit
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))

# Print the results
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)
