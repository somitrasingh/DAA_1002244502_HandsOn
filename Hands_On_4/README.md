## Problem 0: Fibonacci
#### Function Call Stack for fib(5):

fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1) -> fib(0)   
fib(2) -> fib(1) -> fib(0)  
fib(3) -> fib(2) -> fib(1) -> fib(0)  
fib(4) -> fib(3) -> fib(2) -> fib(1) -> fib(0)

## Problem 1: Merging K Sorted Arrays
#### Time Complexity Analysis:
To effectively extract the smallest element from the K sorted arrays, we employ a priority queue (min-heap).
There are always, at most, K entries in the priority queue (one for each array).
We incur 𝑂(log𝐾) every operation for inserting or removing an element from the priority queue for each element in the arrays.
The overall time complexity is 𝑂(𝑁 × 𝐾 × log⁡𝐾) as there are a total of 𝑁 × 𝐾 elements across all arrays, where N is the size of each array and K is the number of arrays.


#### Possible Improvements:

Implement the min-heap with optimized priority queues or libraries like Python’s heapq. Store only necessary data (e.g., tuples of values and indices) to minimize memory overhead. Merge arrays in batches or use multi-threading to speed up the process. For very large data, use external storage techniques or distributed computing frameworks. Apply adaptive algorithms and in-place merging to reduce unnecessary operations and memory usage.


## Problem 2: Removing Duplicates from a Sorted Array
#### Time Complexity Analysis:
We iterate through the array exactly once, comparing each element with its predecessor. This gives a time complexity of:
O(N) where, N is the size of the input array.

#### Possible Improvements:
We can modify the original array instead of creating new array it will help to reduce the space complexity and time complexity.
If the array is already sorted, you could use binary search to find the next unique element, Binary search could be faster for arrays with many duplicates.
