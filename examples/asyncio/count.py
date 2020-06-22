import time


def count():
    print("One")
    time.sleep(.01)
    print("Two")


def main():
    for i in range(0, 100):
        count()


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
