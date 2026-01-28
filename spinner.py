"""
Spinner
"""
import asyncio
from typing import Awaitable

def spin_cursor():
    """
    Symbols to generate a spinning cursor

    Yields:
        str -- next spinning cursor character
    """
    while True:
        for cursor in '|/-\\':
            yield cursor

async def spinner(task: Awaitable[any], delay: float=0.2) -> None:
    """
    Shows a spinning cursor in the standard output while a task gets done

    Arguments:
        task {Awaitable[_T]} -- task to be awaited
    """
    spin = spin_cursor()
    while not task.done():
        print(next(spin), end='\r', flush=True)
        await asyncio.sleep(delay)
    print(" ", end='\r', flush=True)

async def spinner_test(delay: int = 5):
    """
    Async function to test the spinner with a sleep to emulate a blocking task.

    Keyword Arguments:
        delay {int} -- time, in seconds, to sleep (default: {5})
    """
    import time
    print("Spinner test")
    print(f"It will take {delay} seconds")
    loop = asyncio.get_running_loop()
    task = loop.run_in_executor(None, time.sleep, delay)
    await spinner(task)
    print("Test finished")


if __name__ == "__main__":
    asyncio.run(spinner_test(5))
