class MinHeap:
    def __init__(self, data=[]):
        self.heap = []
        if data:
            self.build_min_heap(data)

    # Get index of the parent node using bitwise operators
    def parent(self, i):
        return (i - 1) >> 1  # Equivalent to (i - 1) // 2

    # Get index of the left child node using bitwise operators
    def left(self, i):
        return (i << 1) + 1  # Equivalent to 2 * i + 1

    # Get index of the right child node using bitwise operators
    def right(self, i):
        return (i << 1) + 2  # Equivalent to 2 * i + 2

    # Heapify the element at index i
    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i

        # Check if left child exists and is smaller than current element
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Check if right child exists and is smaller than smallest found so far
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest element is not the parent, swap and heapify the affected sub-tree
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    # Build the heap using the given data
    def build_min_heap(self, data):
        self.heap = data[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)

    # Insert a new element into the heap
    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        # Bubble up the new value to its proper position
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # Pop the root node (minimum value) from the heap
    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Pop from an empty heap")

        root = self.heap[0]
        # Replace the root with the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()  # Remove the last element
        self.heapify(0)  # Restore heap property
        return root

    # Peek at the root node without removing it
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("Peek from an empty heap")
        return self.heap[0]

    # Check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Print the heap (for debugging purposes)
    def __str__(self):
        return str(self.heap)

# Example usage:

if __name__ == "__main__":
    
    # Build the heap from a list of integers
    data = [9, 5, 6, 2, 3, 1, 7]
    heap = MinHeap(data)
    print("Example 1:")
    print("Initial heap:", heap)

    # Pop the root node (smallest element)
    print("Popped element:", heap.pop())
    print("Heap after pop:", heap)

    # Insert new elements
    heap.insert(4)
    heap.insert(8)
    print("Heap after insertions:", heap)

    # Peek at the root (minimum element)
    print("Peek at root:", heap.peek())

    # Pop all elements to demonstrate functionality
    while not heap.is_empty():
        print("Popped element:", heap.pop())
        print("Heap:", heap)

    
## Example 2 
    print("Example 2:")
    # Initial heap construction with integer values
    data = [15, 5, 20, 1, 17, 10, 30]
    heap = MinHeap(data)
    print("Initial heap:", heap)

    # Check if the heap is empty
    print("Is heap empty?", heap.is_empty())

    # Peek at the root element
    print("Peek at root:", heap.peek())

    # Insert elements into the heap
    heap.insert(3)
    heap.insert(2)
    print("Heap after insertions (3, 2):", heap)

    # Pop the root (smallest element)
    print("Popped element:", heap.pop())
    print("Heap after pop:", heap)

    # Pop all elements and display heap after each pop
    while not heap.is_empty():
        print("Popped element:", heap.pop())
        print("Heap:", heap)

    # Final check if the heap is empty
    print("Is heap empty?", heap.is_empty())
