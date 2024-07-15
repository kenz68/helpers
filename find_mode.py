from typing import List, Optional
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMode(self, root: Optional[TreeNode]) -> List[int]:
        leafs = []
        def _get_leaf_nodes( node):
            if node is not None:
                if len(node.children) == 0:
                    leafs.append(node)
                for n in node.children:
                    _get_leaf_nodes(n)
        _get_leaf_nodes(root)