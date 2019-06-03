import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print(f"task {name}: compute factorial for - {i}")
        await asyncio.sleep(1)
        f *= i
    print(f"task {name}: factorial({number}) = {f}")


async def main():
    # schedule three calls concurrently
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())

"""
Outputs
-----------
task A: compute factorial for - 2
task B: compute factorial for - 2
task C: compute factorial for - 2
task A: factorial(2) = 2
task B: compute factorial for - 3
task C: compute factorial for - 3
task B: factorial(3) = 6
task C: compute factorial for - 4
task C: factorial(4) = 24
"""
