def remove_duplicates(sorted_array):
    if not sorted_array:
        return []
    length = len(sorted_array)
    unique_index = 0
    for i in range(1, length):
        if sorted_array[i] != sorted_array[unique_index]:
            unique_index += 1
            sorted_array[unique_index] = sorted_array[i]
    return sorted_array[:unique_index + 1]

arr = input("Enter a sorted array : ")
input_array = list(map(int, arr.split()))
output_array = remove_duplicates(input_array)

print(f"Original array: {input_array}")
print(f"Array after removing the duplicate elements: {output_array}")

'''Input: array = [2, 2, 2, 2, 2]'''
'''Input: array = [1, 2, 2, 3, 4, 4, 4, 5, 5]'''
