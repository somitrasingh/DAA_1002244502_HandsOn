class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'RED'

class RBT:
    def __init__(self):
        self.NULL_LEAF = TreeNode(0)
        self.NULL_LEAF.color = 'BLACK'
        self.root = self.NULL_LEAF

    def add(self, value):
        new_node = TreeNode(value)
        new_node.left = self.NULL_LEAF
        new_node.right = self.NULL_LEAF
        self._bst_insert(new_node)
        self._balance_insert(new_node)

    def _bst_insert(self, node):
        parent_node = None
        current = self.root

        while current != self.NULL_LEAF:
            parent_node = current
            if node.value < current.value:
                current = current.left
            else:
                current = current.right

        node.parent = parent_node
        if parent_node is None:
            self.root = node
        elif node.value < parent_node.value:
            parent_node.left = node
        else:
            parent_node.right = node

    def _balance_insert(self, node):
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'BLACK'

    def remove(self, value):
        node_to_remove = self.find(self.root, value)
        if node_to_remove == self.NULL_LEAF:
            print(f"{value} not found in the Red-Black Tree. Removal not performed.")
            return
        self._remove_node(node_to_remove)

    def _remove_node(self, node):
        original_color = node.color
        if node.left == self.NULL_LEAF:
            temp = node.right
            self._transplant(node, node.right)
        elif node.right == self.NULL_LEAF:
            temp = node.left
            self._transplant(node, node.left)
        else:
            successor = self.minimum(node.right)
            original_color = successor.color
            temp = successor.right
            if successor.parent == node:
                temp.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color

        if original_color == 'BLACK':
            self._balance_remove(temp)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _balance_remove(self, node):
        while node != self.root and node.color == 'BLACK':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self._left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self._right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self._right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == 'BLACK' and sibling.left.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self._left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self._right_rotate(node.parent)
                    node = self.root
        node.color = 'BLACK'

    def find(self, node, value):
        if node == self.NULL_LEAF or node.value == value:
            return node
        if value < node.value:
            return self.find(node.left, value)
        return self.find(node.right, value)

    def minimum(self, node):
        while node.left != self.NULL_LEAF:
            node = node.left
        return node

    def inorder_traversal(self, node, result):
        if node != self.NULL_LEAF:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

    def _left_rotate(self, node):
        temp = node.right
        node.right = temp.left
        if temp.left != self.NULL_LEAF:
            temp.left.parent = node
        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        temp.left = node
        node.parent = temp
        temp.color = 'BLACK'
        node.color = 'RED'

    def _right_rotate(self, node):
        temp = node.left
        node.left = temp.right
        if temp.right != self.NULL_LEAF:
            temp.right.parent = node
        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp
        temp.right = node
        node.parent = temp
        temp.color = 'BLACK'
        node.color = 'RED'

def rbtree_interface():
    rbtree = RBT()
    while True:
        print("\nRed-Black Tree Operations:")
        print("1. Add Node")
        print("2. Remove Node")
        print("3. Find Node")
        print("4. In-order Traversal")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to add: "))
            rbtree.add(value)
            print(f"{value} added.")
        elif choice == 2:
            value = int(input("Enter value to remove: "))
            rbtree.remove(value)
        elif choice == 3:
            value = int(input("Enter value to find: "))
            found = rbtree.find(rbtree.root, value)
            if found != rbtree.NULL_LEAF:
                print(f"{value} found in Red-Black Tree.")
            else:
                print(f"{value} not found in Red-Black Tree.")
        elif choice == 4:
            print("In-order Traversal:", rbtree.inorder_traversal(rbtree.root, []))
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

rbtree_interface()
