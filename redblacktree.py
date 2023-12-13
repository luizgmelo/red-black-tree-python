RED = 1
BLACK = 0

class Node:
    def __init__(self, key, left = None, right = None, parent = None, color = RED):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

class RB:

  def __init__(self):
      self.root = None
    
  def verify_balance(self, root):
    # CASE 1 no rotates
    if root.parent is None:
        root.color = BLACK
        return

    grandParent = root.parent.parent
    if not grandParent:
        return

    if root.parent.color == RED:
        if grandParent.left != root.parent:
            uncle = grandParent.left
        else:
            uncle = grandParent.right

        if uncle.color == RED:
            root.parent.color = BLACK
            uncle.color = BLACK
            grandParent.color = RED

        self.verify_balance(grandParent)

  def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.root.color = BLACK
            return
            
        return self.__insertNode(key, self.root)

  def __insertNode(self, key, root):
    if root.key > key:
        if root.left is None:
            root.left = Node(key)
            root.left.parent = root
            return self.verify_balance(root.left)
        return self.__insertNode(key, root.left)
    if root.key < key:
        if root.right is None:
            root.right = Node(key)
            root.right.parent = root
            return self.verify_balance(root.right)
        return self.__insertNode(key, root.right)


rb = RB()
