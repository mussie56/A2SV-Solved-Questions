# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        count = 0
        def helper(root):
            nonlocal count
            if not root:
                return [0,0]
            
            left = helper(root.left)
            right = helper(root.right)
            size = left[0]+right[0]+1
            coins = root.val+right[1]+left[1]
            count += abs(size - coins)

            return [size, coins]
            
        helper(root)
        return count
            
        #     if not root:
        #         return 0

        #     left = helper(root.left)
        #     right = helper(root.right)
        #     if left > 0:
        #         self.count += left
        #     if right > 0:
        #         self.count += right

        #     if not root.val:
        #         return left+right-1
        #     else:
        #         self.count+=root.val-1
        #         return left+right+root.val-1
        # return self.count