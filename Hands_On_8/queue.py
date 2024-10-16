class Queue:
    def __init__(self, capacity):
        self.queue = [0] * capacity  
        self.start = 0
        self.end = 0
        self.capacity = capacity
        self.element_count = 0 
    def is_empty(self):
        return self.element_count == 0

    def is_full(self):
        return self.element_count == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full, cannot add more elements!")
            return
        self.queue[self.end] = data
        self.end = (self.end + 1) % self.capacity  
        self.element_count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty, cannot remove element!")
        removed_value = self.queue[self.start]
        self.start = (self.start + 1) % self.capacity  
        self.element_count -= 1
        return removed_value

    def front_value(self):
        if self.is_empty():
            raise Exception("Queue is empty, no front element!")
        return self.queue[self.start]

    def show_queue(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            elements = []
            i = self.start
            for _ in range(self.element_count):
                elements.append(self.queue[i])
                i = (i + 1) % self.capacity  
            print("Current Queue:", elements)

# Example Usage
circular_queue = Queue(5)
circular_queue.enqueue(10)
circular_queue.enqueue(20)
circular_queue.enqueue(30)
circular_queue.enqueue(40)
circular_queue.enqueue(50)
circular_queue.enqueue(60)  # Queue is full
circular_queue.show_queue()
print("Removed:", circular_queue.dequeue())
print("Front element:", circular_queue.front_value())
circular_queue.show_queue()
