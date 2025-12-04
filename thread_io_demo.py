import time
import threading

URLS = [f"url-{i}" for i in range(20)]


def download(url: str) -> None:
    """Имитация I/O-операции."""
    time.sleep(1)
    print(f"Downloaded {url}")


def run_sequential():
    for url in URLS:
        download(url)


def run_with_threads():
    threads = []

    for url in URLS:
        t = threading.Thread(target=download, args=(url,))
        t.start()
        threads.append(t)

    # Дожидаемся завершения всех потоков
    for t in threads:
        t.join()


def measure(fn, label: str):
    start = time.perf_counter()
    fn()
    end = time.perf_counter()
    print(f"{label}: {end - start:.2f} seconds")


if __name__ == "__main__":
    print("Sequential run:")
    measure(run_sequential, "Sequential")

    print("\nThreaded run:")
    measure(run_with_threads, "Threaded")
