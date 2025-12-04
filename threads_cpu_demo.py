import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def cpu_heavy(n: int) -> int:
    s = 0
    for i in range(n):
        s += i * i
    return s


def run_sequential(tasks, n):
    for _ in range(tasks):
        cpu_heavy(n)


def run_thread_pool(tasks, n, workers=4):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(cpu_heavy, n) for _ in range(tasks)]
        for f in as_completed(futures):
            _ = f.result() 


def measure(fn, label, *args):
    start = time.perf_counter()
    fn(*args)
    end = time.perf_counter()
    print(f"{label}: {end - start:.2f} seconds")


if __name__ == "__main__":
    TASKS = 8
    N = 50_000_000 

    print("Sequential run:")
    measure(run_sequential, "Sequential", TASKS, N)

    print("\nThreadPool run:")
    measure(run_thread_pool, "ThreadPool", TASKS, N)
