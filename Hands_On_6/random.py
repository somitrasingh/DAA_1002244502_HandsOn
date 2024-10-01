import random

def random_quicksort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = random.choice(a)
        less_than_pivot = [x for x in a if x < pivot]
        equal_to_pivot = [x for x in a if x == pivot]
        greater_than_pivot = [x for x in a if x > pivot]
        
        return random_quicksort(less_than_pivot) + equal_to_pivot + random_quicksort(greater_than_pivot)


a = [10, 80, 30, 90, 40, 50, 70]
sorted_arr_random = random_quicksort(a)
print("Sorted array (Randomized QuickSort):", sorted_arr_random)
