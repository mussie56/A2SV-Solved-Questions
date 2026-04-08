# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maxx = nums.index(max(nums))
        root = TreeNode(nums[maxx])
        root.left = self.constructMaximumBinaryTree(nums[:maxx])
        root.right = self.constructMaximumBinaryTree(nums[maxx+1:])
        return root