import time
import asyncio


async def count():
    # print("One")
    await asyncio.sleep(1)  # <-- I/O Bound Tasks
    # print("Two")


async def main():
    await asyncio.gather(*[count() for i in range(0, 1000000)])


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


"""
1 I/O Bound Task - 1.00 Seconds
10 I/O Bound Task - 1.01 Seconds
100 I/O Bound Task - 1.01 Seconds
1,000 I/O Bound Task - 1.02 Seconds
10,000 I/O Bound Task - 1.15 Seconds
100,000 I/O Bound Task - 3.27 Seconds
1,000,000 I/O Bound Task - 35.88 Seconds
"""
