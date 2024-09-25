
A generic heap structure, allowing for various data types (can store floats, int).
The min-heap attribute states that the root is always the smallest element.

Operations on heaps:
Inserting new elements into the heap.
Removing the root element and adding the heap property.
creating a min-heap out of a random or unsorted array.
obtaining the heap's root element without removal.

# output
#Heap structure after building:
#Integer values: [1, 3, 5]
#Float values: [2.1, 4.5, 6.3]

#Heap after adding 0.8:
#Integer values: [1, 3, 5]
#Float values: [0.8, 2.1, 6.3, 4.5]

#Heap after adding 7:
#Integer values: [1, 3, 5, 7]
#Float values: [0.8, 2.1, 6.3, 4.5]

#Removed the smallest integer value: 1

#Heap after removing the smallest integer value:
#Integer values: [3, 7, 5]
#Float values: [0.8, 2.1, 6.3, 4.5]

#Removed the smallest float value: 0.8

#Heap after removing the smallest float value:
#Integer values: [3, 7, 5]
#Float values: [2.1, 4.5, 6.3]
