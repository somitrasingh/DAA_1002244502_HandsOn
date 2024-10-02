import time
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(2000)

def quicksort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[-1]
        less_than_pivot = [x for x in a[:-1] if x <= pivot]
        greater_than_pivot = [x for x in a[:-1] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def measure_time(quicksort, arr):
    start_time = time.time()
    quicksort(arr)
    return time.time() - start_time


def generate_best_case(n):
    return list(range(n))

def generate_worst_case(n):
    return list(range(n, 0, -1))

def generate_average_case(n):
    return [random.randint(0, 10000) for _ in range(n)]

n_values = [100, 500, 1000, 1500]

best_times = []
for n in n_values:
    arr_best = generate_best_case(n)
    time_taken = measure_time(quicksort, arr_best)
    best_times.append(time_taken)
    print(f"Best case, n={n}, time: {time_taken:.6f} seconds")

worst_times = []
for n in n_values:
    arr_worst = generate_worst_case(n)
    time_taken = measure_time(quicksort, arr_worst)
    worst_times.append(time_taken)
    print(f"Worst case, n={n}, time: {time_taken:.6f} seconds")

avg_times = []
for n in n_values:
    arr_avg = generate_average_case(n)
    time_taken = measure_time(quicksort, arr_avg)
    avg_times.append(time_taken)
    print(f"Average case, n={n}, time: {time_taken:.6f} seconds")

plt.plot(n_values, best_times, label="Best Case", marker='o')
plt.plot(n_values, worst_times, label="Worst Case", marker='o')
plt.plot(n_values, avg_times, label="Average Case", marker='o')

plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('QuickSort Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()
