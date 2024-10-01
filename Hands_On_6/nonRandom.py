def quicksort(a):
   
    if len(a) <= 1:
        return a
    else:
        
        pivot = a[-1]
        less_than_pivot = [x for x in a[:-1] if x <= pivot]
        greater_than_pivot = [x for x in a[:-1] if x > pivot]
        
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


a = [10, 80, 30, 90, 40, 50, 70]
sorted_arr = quicksort(a)
print("Sorted array (Non-random QuickSort):", sorted_arr)


