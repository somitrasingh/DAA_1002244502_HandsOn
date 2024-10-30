class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._recursive_add(self.root, key)

    def _recursive_add(self, current, key):
        if key < current.key:
            if not current.left:
                current.left = Node(key)
            else:
                self._recursive_add(current.left, key)
        else:
            if not current.right:
                current.right = Node(key)
            else:
                self._recursive_add(current.right, key)

    def find(self, key):
        return self._recursive_find(self.root, key)

    def _recursive_find(self, current, key):
        if not current or current.key == key:
            return current
        if key < current.key:
            return self._recursive_find(current.left, key)
        return self._recursive_find(current.right, key)

    def remove(self, key):
        self.root = self._recursive_remove(self.root, key)

    def _recursive_remove(self, current, key):
        if not current:
            return current

        if key < current.key:
            current.left = self._recursive_remove(current.left, key)
        elif key > current.key:
            current.right = self._recursive_remove(current.right, key)
        else:
            if not current.left:
                return current.right
            if not current.right:
                return current.left
            
            min_larger_node = self._find_min(current.right)
            current.key = min_larger_node.key
            current.right = self._recursive_remove(current.right, min_larger_node.key)
        
        return current

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def traverse_inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, current, result):
        if current:
            self._inorder(current.left, result)
            result.append(current.key)
            self._inorder(current.right, result)
        return result

# Testing the modified Binary Search Tree with the updated variable names
bstree = BST()
for num in [50, 30, 20, 40, 70, 60, 80]:
    bstree.add(num)

# Inorder traversal before and after deletions
initial_traversal = bstree.traverse_inorder()

# Deletion tests
bstree.remove(20)
traversal_after_remove_20 = bstree.traverse_inorder()

bstree.remove(30)
traversal_after_remove_30 = bstree.traverse_inorder()

bstree.remove(50)
traversal_after_remove_50 = bstree.traverse_inorder()

# Output results
print("In-Order Traversal (Initial):", initial_traversal)           #Output: In-Order Traversal (Initial): [20, 30, 40, 50, 60, 70, 80]
print("In-Order Traversal after Removing 20:", traversal_after_remove_20)       #Output: In-Order Traversal after Removing 20: [30, 40, 50, 60, 70, 80]
print("In-Order Traversal after Removing 30:", traversal_after_remove_30)       #Output: In-Order Traversal after Removing 30: [40, 50, 60, 70, 80]
print("In-Order Traversal after Removing 50:", traversal_after_remove_50)       #Output: In-Order Traversal after Removing 50: [40, 60, 70, 80]

