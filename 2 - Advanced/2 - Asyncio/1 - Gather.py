import asyncio
import time

async def show_message(msg: str):
    await asyncio.sleep(1)  # Await the asynchronous sleep
    print(msg)

async def main():
    # Prepare a list of messages
    messages = ["Hi, there!", "Welcome!", "How are you?", "Goodbye!"]
    
    # Create a list of coroutines
    tasks = [show_message(msg) for msg in messages]
    
    # Run all tasks concurrently (using * unpack operator)
    await asyncio.gather(*tasks)

start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"Execution Time: {round((end - start)*1000)}ms")

# Even tough there are 4 asynchronous functions with 1s delay,
# the overall execution time is around 1s (cause they can run concurrently)