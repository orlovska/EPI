import unittest
import context
from python_code import is_binary_tree_balanced
from python_code import BinaryTreeNode

class N:
    
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right 

#Height-balanced
tree1 = N(1, N(3, N(2), N(3)), N(5))
tree2 = N(10, N(6, N(4), N(5, N(3), N(7))), N(5, N(6), N(7, N(7), N(3))))
tree3 = N(6)
tree4 = N(None)
#Height-anbalanced 
tree5 = N(3, N(9, N(8, N(7, N(4), None), None), None), N(6))
tree6 = N(7, None, N(6, N(6), N(9)))
tree7 = N(7, N((6, N(6), N(9))), None)

class BasicTest(unittest.TestCase):

    def test_empty_binary_tree(self):
        self.assertEqual(is_binary_tree_balanced(tree4), True)
    
    def test_one_node_tree(self):
        self.assertEqual(is_binary_tree_balanced(tree3), True)

    def test_balanced_trees(self):
        self.assertEqual(is_binary_tree_balanced(tree1), True)
        self.assertEqual(is_binary_tree_balanced(tree2), True)

    def test_anbalanced_trees(self):
        self.assertEqual(is_binary_tree_balanced(tree5), False)
        self.assertEqual(is_binary_tree_balanced(tree6), False)
        self.assertEqual(is_binary_tree_balanced(tree7), False)


if __name__=='__main__':
    unittest.main()   