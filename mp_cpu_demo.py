import time
from multiprocessing import Pool, cpu_count

def cpu_heavy(n: int) -> int:
    # Просто тяжёлый цикл
    s = 0
    for i in range(n):
        s += i * i
    return s


def run_sequential(tasks, n):
    for _ in range(tasks):
        cpu_heavy(n)


def run_multiprocessing(tasks, n):
    with Pool(processes=cpu_count()) as pool:
        pool.map(cpu_heavy, [n] * tasks)


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

    print("\nMultiprocessing run:")
    measure(run_multiprocessing, "Multiprocessing", TASKS, N)
