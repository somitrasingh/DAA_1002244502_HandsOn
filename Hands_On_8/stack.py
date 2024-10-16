class Stack:
    def __init__(self, capacity):
        self.container = [0] * capacity  
        self.pointer = -1  
        self.capacity = capacity

    def is_empty(self):
        return self.pointer == -1

    def is_full(self):
        return self.pointer == self.capacity - 1

    def push(self, element):
        if self.is_full():
            print("Stack Overflow - Unable to push more elements")
            return
        self.pointer += 1
        self.container[self.pointer] = element

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow - No elements to pop")
        removed_element = self.container[self.pointer]
        self.pointer -= 1
        return removed_element

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty - No top element")
        return self.container[self.pointer]

    def display(self):
        if self.is_empty():
            print("The stack is currently empty")
        else:
            print("Stack content:", self.container[:self.pointer + 1])

# Example Usage
stack_instance = Stack(5)
stack_instance.push(10)
stack_instance.push(20)
stack_instance.push(30)
stack_instance.push(40)
stack_instance.push(50)
stack_instance.push(60)  
stack_instance.display()
print("Popped:", stack_instance.pop())
print("Top element:", stack_instance.peek())
stack_instance.display()
