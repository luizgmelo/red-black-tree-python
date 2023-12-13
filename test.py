import unittest
from redblacktree import RB, Node, RED, BLACK

class RedBlackTree(unittest.TestCase):
    def setUp(self):
        self.rb = RB()

    def test_insert(self):
        # CASE 1 no rotates
        self.rb.insert(3)
        self.rb.insert(1)
        self.rb.insert(4)
        self.rb.insert(0)
        """
                3B
            1B      4B
           0R
        """
        root = self.rb.root
        leftChild = root.left
        rightChild = root.right

        self.assertEqual(root.key, 3)
        self.assertEqual(root.parent, None)
        self.assertEqual(root.color, BLACK)

        self.assertEqual(leftChild.key, 1)
        self.assertEqual(leftChild.parent, root)
        self.assertEqual(leftChild.color, BLACK)

        self.assertEqual(rightChild.key, 4)
        self.assertEqual(rightChild.parent, root)
        self.assertEqual(rightChild.color, BLACK)

        self.assertEqual(leftChild.left.key, 0)
        self.assertEqual(leftChild.left.parent, leftChild)
        self.assertEqual(leftChild.left.color, RED)

if __name__ == "__main__":
   unittest.main()

