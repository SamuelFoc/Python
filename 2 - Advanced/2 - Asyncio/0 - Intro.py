import asyncio
import time

async def show_message(msg: str):
    await asyncio.sleep(1)
    print(msg)

start = time.perf_counter()
asyncio.run(show_message("Hi, there!"))
end = time.perf_counter()

print(f"Execution Time: {round((end - start)*1000)}ms")