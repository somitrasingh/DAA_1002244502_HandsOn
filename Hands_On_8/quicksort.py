
def partition(arr, left, right):
    pivot = arr[right]
    idx = left - 1
    for curr in range(left, right):
        if arr[curr] <= pivot:
            idx += 1
            arr[idx], arr[curr] = arr[curr], arr[idx]
    arr[idx + 1], arr[right] = arr[right], arr[idx + 1]
    return idx + 1


def quicksort(arr, left, right):
    if left < right:
        pivot_idx = partition(arr, left, right)
        quicksort(arr, left, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, right)


def ith_order_statistic(arr, left, right, ith):
    if left == right:  
        return arr[left]

    pivot_idx = partition(arr, left, right)

    elements_in_left = pivot_idx - left + 1

    if elements_in_left == ith:
        return arr[pivot_idx]
    elif ith < elements_in_left:
        return ith_order_statistic(arr, left, pivot_idx - 1, ith)
    else:
        return ith_order_statistic(arr, pivot_idx + 1, right, ith - elements_in_left)


# Example usage
if __name__ == "__main__":
    arr = [8, 5, 23, 10, 19, 6]
    ith = 4  
    size = len(arr)
    result = ith_order_statistic(arr, 0, size - 1, ith)
    print(f"The {ith}th smallest element is: {result}")
