## Problem 3

The pivot divides the array into two about equal sections in the average scenario. Thus, k is around n/2, which results in:


T(n) = 2T(n/2) + O(n)

The divide-and-conquer recurrence master theorem can be applied to solve this recurrence relation. The recurrence usually has this broad form:

T(n) = O(n^d) + aT(n/b)

We have a = 2, b = 2, and d = 1 in this instance because the partitioning takes O(n) linear time.

The master theorem is applied by comparing n^d with n^(logb(a)):
logb(a) = log2(2) = 1 for d = 1.

Given that d = logb(a), the master theorem provides the following solution in this situation:
    
T(n) = O(n^d logn) = O(nlogn).

The Quicksort version without random pivot has an average time complexity of O(nlogn). This is because the pivot, on average, divides the array into two about equal pieces, resulting in a logarithmic depth of recursion, where the partitioning time for each level of recursion is linear. As a result, O(nlogn) is the average runtime complexity overall.


