class ListNode:
    def __init__(self, data, next_index=-1):
        self.data = data
        self.next_index = next_index  

class SingleLinkedList:
    def __init__(self, capacity):
        self.nodes = [None] * capacity  
        self.head_index = -1  
        self.capacity = capacity
        self.free_index = 0  

    def add_to_end(self, data):
        if self.free_index == self.capacity:
            raise OverflowError("No more space in the list!")
        new_node = ListNode(data, -1)
        if self.head_index == -1:
            self.head_index = self.free_index
        else:
            current_index = self.head_index
            
            while self.nodes[current_index].next_index != -1:
                current_index = self.nodes[current_index].next_index
            self.nodes[current_index].next_index = self.free_index
        self.nodes[self.free_index] = new_node
        self.free_index += 1

    def remove_from_start(self):
        if self.head_index == -1:
            raise Exception("List is empty!")
        data = self.nodes[self.head_index].data
        self.head_index = self.nodes[self.head_index].next_index
        return data

    def remove_from_end(self):
        if self.head_index == -1:
            raise Exception("List is empty!")
        if self.nodes[self.head_index].next_index == -1:
            data = self.nodes[self.head_index].data
            self.head_index = -1
            return data
        current_index = self.head_index
        
        while self.nodes[self.nodes[current_index].next_index].next_index != -1:
            current_index = self.nodes[current_index].next_index
        data = self.nodes[self.nodes[current_index].next_index].data
        self.nodes[current_index].next_index = -1
        return data

    def print_list(self):
        if self.head_index == -1:
            print("The list is currently empty.")
        else:
            current_index = self.head_index
            elements = []
            while current_index != -1:
                elements.append(self.nodes[current_index].data)
                current_index = self.nodes[current_index].next_index
            print("Current Linked List:", elements)

# Example Usage
static_list = SingleLinkedList(5)
static_list.add_to_end(10)
static_list.add_to_end(20)
static_list.add_to_end(30)
static_list.add_to_end(40)
static_list.add_to_end(50)
static_list.print_list()
print("Removed from start:", static_list.remove_from_start())
print("Removed from end:", static_list.remove_from_end())
static_list.print_list()
