# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ans.append(root.val)
            ans.append(root.val+left+right)
            ans.append(root.val+max(left,right,0))
            return ans[-1]
        ans.append(dfs(root))
        ans.sort()
        return ans[-1]