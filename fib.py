from functools import lru_cache
import time
import matplotlib.pyplot as plt

times = []
n_values = []

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        times.append(execution_time)
        n_values.append(args[0])
        
        print(f"Finished in {execution_time:.8f}s: f({args[0]}) -> {result}")
        return result
    return wrapper

@lru_cache
@timer
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    fib(100)
    
    sorted_points = [(n_values[i], times[i]) for i in range(len(n_values))]
    sorted_points.sort()

    sorted_n = [point[0] for point in sorted_points]
    sorted_times = [point[1] for point in sorted_points]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_n, sorted_times)
    
    plt.title('Fibonacci')
    plt.xlabel('Fibonacci Number')
    plt.ylabel('Seconds')
    plt.grid(True, alpha=0.5)

    plt.tight_layout()
    plt.savefig('fib.png')
    plt.show()