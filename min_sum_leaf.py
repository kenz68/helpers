from typing import Optional
import string


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(root: Optional[TreeNode], arr, ans):
            if not root:
                return
            arr.append(root.val)
            if root.left is None and root.right is None:
                ans.append(arr.copy())
                del arr[-1]
                return
            helper(root.left, arr, ans)
            helper(root.right, arr, ans)
            del arr[-1]
        p = []
        if not root:
            return [[]]
        arr = []
        helper(root, arr, p)
        lw = string.ascii_lowercase
        mVal = ''.join([lw[i] for i in p[0][::-1]])
        for val in p:
            mVal = min(mVal, ''.join([lw[i] for i in val[::-1]]))

        return mVal


node = TreeNode(val=4, left=TreeNode(9, left=TreeNode(5),
                right=TreeNode(1)), right=TreeNode(0))
s = Solution()
p = s.smallestFromLeaf(node)
print(p)
