class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [0] * self.capacity

    def _resize(self, new_capacity):
        temp_array = [0] * new_capacity
        for i in range(self.size):
            temp_array[i] = self.array[i]
        self.array = temp_array
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1

    def remove_last(self):
        if self.size > 0:
            self.size -= 1
            if self.size <= self.capacity // 4:
                self._resize(self.capacity // 2)

    def get_element(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of range")

    def set_element(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")

    def current_size(self):
        return self.size

    def current_capacity(self):
        return self.capacity

    def display(self):
        print([self.array[i] for i in range(self.size)])

if __name__ == "__main__":
    dyn_array = DynamicArray()

    dyn_array.append(1)
    dyn_array.append(2)
    dyn_array.append(3)
    dyn_array.append(4)

    print("Array elements:", end=" ")
    dyn_array.display()

    print("Element at index 2:", dyn_array.get_element(2))

    dyn_array.set_element(1, 10)
    print("Array elements after setting index 1 to 10:", end=" ")
    dyn_array.display()

    dyn_array.remove_last()
    print("Array elements after remove_last:", end=" ")
    dyn_array.display()

    print("Size:", dyn_array.current_size(), ", Capacity:", dyn_array.current_capacity())
