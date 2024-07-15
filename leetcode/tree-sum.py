# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def addNode(curr: Optional[TreeNode], val: int, depth: int):
            if depth > 2:
                depth -= 1
                addNode(curr=curr.left, val=val, depth=depth)
                addNode(curr=curr.right, val=val, depth=depth)
                return
            if depth == 2:
                left = TreeNode(val=val, left=curr.left)
                curr.left = left
                right = TreeNode(val=val, right=curr.right)
                curr.right = right
                return
        head = root
        addNode(curr=head, val=val, depth=depth)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def r2l(curr: Optional[TreeNode], sm: int):
            if not curr:
                return 0
            sm = sm*10 + curr.val
            if not curr.left and not curr.right:
                return sm
            return r2l(curr.left, sm) + r2l(curr.right, sm)
        return r2l(root, 0)

    def helper(self, root: Optional[TreeNode], arr, ans):
        if not root:
            return

        arr.append(root.val)

        if root.left is None and root.right is None:
            # This will be only true when the node is leaf node
            # and hence we will update our ans array by inserting
            # array arr which have one unique path from root to leaf
            ans.append(arr.copy())
            del arr[-1]
            # after that we will return since we don't want to check after leaf node
            return

        # recursively going left and right until we find the leaf and updating the arr
        # and ans array simultaneously
        self.helper(root.left, arr, ans)
        self.helper(root.right, arr, ans)
        del arr[-1]

    def Paths(self, root):
        # creating answer in which each element is a array
        # having one unique path from root to leaf
        ans = []
        # if root is null then there is no further action require so return
        if not root:
            return [[]]
        arr = []
        # arr is a array which will have one unique path from root to leaf
        # at a time.arr will be updated recursively
        self.helper(root, arr, ans)
        # after helper function call our ans array updated with paths so we will return ans array
        return ans


# node = TreeNode(val=4, left=TreeNode(9, left=TreeNode(5),
#                 right=TreeNode(1)), right=TreeNode(0))
# s = Solution()
# # print(s.sumNumbers(node))
# print(s.Paths(node))
# s.addOneRow(root=node, val=10, depth=1)
# print(s.Paths(node))
# print(s.sumNumbers(node))

nd = TreeNode(val=4,
              left=TreeNode(2, left=TreeNode(3), right=TreeNode(1)),
              right=TreeNode(6, left=TreeNode(5))
              )
s = Solution()
print(s.Paths(nd))
s.addOneRow(root=nd, val=1, depth=2)
print(s.Paths(nd))
