import random
import asyncio


ANSI_COLORS = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def makerandom(idx: int, threshold: int = 6) -> int:
    print(f"{ANSI_COLORS[idx+1]}Initiated makerandom({idx})")
    i = random.randint(0, 10)
    while i <= threshold:
        print(
            f"{ANSI_COLORS[idx+1]}makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(
        f"{ANSI_COLORS[idx+1]}-->Finished makerandom({idx}) == {i}{ANSI_COLORS[0]}")
    return i


async def main():
    return await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(0, 3)))


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    res = asyncio.run(main())
    print(res)
    elapsed = time.perf_counter() - s
    print(f"elpased - {elapsed:0.2f} seconds")
