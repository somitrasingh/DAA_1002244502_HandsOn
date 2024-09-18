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

###### Divide and Conquer Approach:
You could divide and conquer by merging arrays two at a time rather than employing a priority queue. The amount of times you merge from K to logK would decrease as a result.
O(N×KlogK) would still be the time complexity, but because there would be less comparisons made in the heap, it might operate a little bit better in reality.

###### Parallel Processing:
Performance can be greatly increased by parallelizing the merging procedure across several processors or threads if you are working with very large arrays.You can divide the arrays among multiple threads and merge their results in parallel.


##### External Merge Sort:
An external merge sort can be utilized if the arrays are too big to fit in memory. Parts of the data would be sorted in memory and then combined using a disk-based merge process. Using this will help manage big datasets.


## Problem 2: Removing Duplicates from a Sorted Array
#### Time Complexity Analysis:
We iterate through the array exactly once, comparing each element with its predecessor. This gives a time complexity of:
O(N) where, N is the size of the input array.

#### Possible Improvements:
##### Memory Usage:
Currently, the answer changes the input array. For the outcome, you could allocate a new array if memory consumption is not an issue. While code clarity might be enhanced, space complexity would rise from O(1) to O(N).

##### Handling Large Arrays:
Consider stream processing the array if memory is an issue and you have very big sorted arrays. Rather than putting the entire array into memory at once, you can handle portions of the array one at a time.
