#Given K sorted arrays of size N each, the task is to merge them all maintaining their sorted order.
num_arrays = int(input("Enter number of arrays (K) = "))
num_elements = int(input("Enter number of elements in each array (N) = "))  # N is unused in logic
input_arrays = [] 
combined_array = [] 
def insertion_sort(arr): 
    for i in range(1, len(arr)):  
        current_element = arr[i] 
        j = i - 1 
        while j >= 0:
            if arr[j] > current_element:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = current_element
    return arr

for _ in range(num_arrays):  
    user_input = list(map(int, input("Enter sorted array: ").split()))
    input_arrays.append(user_input)

for array in input_arrays:  
    combined_array.extend(array)

print("Merged array in a sorted order:", insertion_sort(combined_array))


'''Input: K = 3, N =  4
array1 = [1,3,5,7]
array2 = [2,4,6,8]
array3 = [0,9,10,11]
Output: [0,1,2,3,4,5,6,7,8,9,10,11]'''

'''Input: K = 3, N =  3
array1 = [1,3,7]
array2 = [2,4,8]
array3 = [9,10,11]
Output: [1,2,3,4,7,8,9,10,11]'''
