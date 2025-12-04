import asyncio
import time

URLS = [f"url-{i}" for i in range(20)]


async def download_async(url: str) -> None:
    """Имитация I/O-операции в асинхронном стиле."""
    await asyncio.sleep(1)
    print(f"Downloaded {url}")


async def run_async():
    tasks = [download_async(url) for url in URLS]
    await asyncio.gather(*tasks)


def measure_sync(fn, label: str):
    start = time.perf_counter()
    fn()
    end = time.perf_counter()
    print(f"{label}: {end - start:.2f} seconds")


def run_sequential():
    for url in URLS:
        time.sleep(1)
        print(f"Downloaded {url}")


if __name__ == "__main__":
    print("Sequential run:")
    measure_sync(run_sequential, "Sequential")

    print("\nAsync run:")
    start = time.perf_counter()
    asyncio.run(run_async())
    end = time.perf_counter()
    print(f"Async: {end - start:.2f} seconds")
