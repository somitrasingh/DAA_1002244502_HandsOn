class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.node_height = 1

class AVL:
    def __init__(self):
        self.root_node = None

    def add(self, val):
        self.root_node = self._recursive_add(self.root_node, val)

    def _recursive_add(self, current, val):
        if not current:
            return Node(val)
        
        if val < current.val:
            current.left_child = self._recursive_add(current.left_child, val)
        else:
            current.right_child = self._recursive_add(current.right_child, val)
        
        current.node_height = 1 + max(self._calculate_height(current.left_child), self._calculate_height(current.right_child))
        
        balance_factor = self._calculate_balance(current)
        
        if balance_factor > 1:
            if val < current.left_child.val:
                return self._rotate_to_right(current)  
            else:
                current.left_child = self._rotate_to_left(current.left_child)
                return self._rotate_to_right(current)  

        if balance_factor < -1:
            if val > current.right_child.val:
                return self._rotate_to_left(current)  
            else:
                current.right_child = self._rotate_to_right(current.right_child)
                return self._rotate_to_left(current)  
        return current

    def _rotate_to_right(self, root):
        new_root = root.left_child
        temp_subtree = new_root.right_child
        
        new_root.right_child = root
        root.left_child = temp_subtree
        
        root.node_height = 1 + max(self._calculate_height(root.left_child), self._calculate_height(root.right_child))
        new_root.node_height = 1 + max(self._calculate_height(new_root.left_child), self._calculate_height(new_root.right_child))
        
        return new_root

    def _rotate_to_left(self, root):
        new_root = root.right_child
        temp_subtree = new_root.left_child
        
        new_root.left_child = root
        root.right_child = temp_subtree
        
        root.node_height = 1 + max(self._calculate_height(root.left_child), self._calculate_height(root.right_child))
        new_root.node_height = 1 + max(self._calculate_height(new_root.left_child), self._calculate_height(new_root.right_child))
        
        return new_root

    def _calculate_height(self, node):
        if not node:
            return 0
        return node.node_height

    def _calculate_balance(self, node):
        if not node:
            return 0
        return self._calculate_height(node.left_child) - self._calculate_height(node.right_child)

# Test cases
avl_tree = AVL()
avl_tree.add(5)
avl_tree.add(3)
avl_tree.add(7)
print(avl_tree.root_node.val)  # Output: 5
print(avl_tree.root_node.left_child.val)  # Output: 3
print(avl_tree.root_node.right_child.val)  # Output: 7
