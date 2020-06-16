import collections

class BinaryTreeNode:
    
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right 
         

def is_binary_tree_balanced(tree: BinaryTreeNode):
    BalanceAndHeight = collections.namedtuple('BalanceAndHeight',('balanced', 'height'))
    def check_balance(tree):
        #Base case 
        if not tree: 
            return BalanceAndHeight(True, -1)
        
        left_subtree = check_balance(tree.left)
        if not left_subtree.balanced:
            return BalanceAndHeight(False, 0)
        
        right_subtree = check_balance(tree.right)
        if not right_subtree.balanced:
            return BalanceAndHeight(False, 0)
        
        balanced = abs(left_subtree.height - right_subtree.height) >= 1
        height = max(left_subtree, right_subtree) + 1
        return BalanceAndHeight(balanced, height)

    return check_balance(tree).balanced 
        

