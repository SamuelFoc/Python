class Logger:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls):   # cls refers to the Logger class itself
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)  # Create a new instance
            cls._instance.log_file = "application.log"  # Initialize the log file
        return cls._instance  # Return the existing instance

    def log(self, message: str):
        with open(self.log_file, "a") as file:
            file.write(f"{message}\n")

# Example usage of the Singleton pattern
if __name__ == "__main__":
    # Attempt to create multiple instances of Logger
    logger1 = Logger()
    logger2 = Logger()

    # Check if both references point to the same instance
    print(f"Logger1 ID: {id(logger1)}")
    print(f"Logger2 ID: {id(logger2)}")
    
    # Log messages using the logger
    logger1.log("This is the first log message.")
    logger2.log("This is the second log message.")
    
    # Both logger1 and logger2 should point to the same instance
    assert logger1 is logger2, "Logger instances are not the same!"

    print("Both logger instances are the same.")
