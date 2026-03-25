# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> int:
            if not root:
                return float('inf')
            if not root.left and not root.right:
                return 1
            left = helper(root.left)
            right = helper(root.right)

            return min(left,right)+1

        res = helper(root)
        return 0 if res == float('inf') else res