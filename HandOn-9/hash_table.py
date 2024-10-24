class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, key, value):
        node = Node(key, value)
        if self.head is None:  
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def delete(self, key):
        node = self.search(key)
        if node is None:
            return
        if node.prev:  
            node.prev.next = node.next
        else: 
            self.head = node.next
        if node.next:  
            node.next.prev = node.prev
        else:  
            self.tail = node.prev

    def display(self):
        current = self.head
        while current:
            print(f"[{current.key}: {current.value}]", end=" ")
            current = current.next
        print()

class HashTable:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.load_threshold = 0.75
        self.shrink_threshold = 0.25
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]

    def compute_hash(self, key):
        fractional = (key * 0.618033) % 1
        return int(self.capacity * fractional) % self.capacity

    def insert(self, key, value):
        index = self.compute_hash(key)
        node = self.buckets[index].search(key)
        if node:  
            node.value = value
        else:  
            self.buckets[index].add_node(key, value)
            self.size += 1
            if self.size / self.capacity > self.load_threshold:  
                self.resize(self.capacity * 2)

    def get(self, key):
        index = self.compute_hash(key)
        node = self.buckets[index].search(key)
        if node:
            return node.value
        else:
            raise KeyError("Key not found!")

    def remove(self, key):
        index = self.compute_hash(key)
        self.buckets[index].delete(key)
        self.size -= 1
        if self.capacity > 4 and self.size / self.capacity < self.shrink_threshold:  
            self.resize(self.capacity // 2)

    def resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            current = bucket.head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def show_table(self):
        for i in range(self.capacity):
            print(f"Bucket {i}: ", end="")
            self.buckets[i].display()

def main():
    hash_table = HashTable()
    while True:
        print("\nHash Table Menu:")
        print("1. Insert")
        print("2. Get")
        print("3. Remove")
        print("4. Display hash table")
        print("5. Exit")
        choice = input("Enter your option: ")

        if choice == '1':
            key = int(input("Enter key to add: "))
            value = int(input("Enter value to add: "))
            hash_table.insert(key, value)
            print(f"Added ({key}, {value})")

        elif choice == '2':
            key = int(input("Enter key to retrieve: "))
            try:
                value = hash_table.get(key)
                print(f"Value for key {key} is {value}")
            except KeyError:
                print("Key not found!")

        elif choice == '3':
            key = int(input("Enter key to remove: "))
            hash_table.remove(key)
            print(f"Key {key} removed")

        elif choice == '4':
            print("Hash Table:")
            hash_table.show_table()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
