# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = []
        def helper(root):
            if not root:
                return [0,float('inf'),float('-inf')] #summ,min right,max left
            left = helper(root.left)
            right = helper(root.right)

            if root.val > left[2] and root.val < right[1]:
                summ = left[0]+right[0]+root.val
                # if summ > 0:
                ans.append(summ)
                # return [summ,max(root.val,right[2]),min(root.val,left[1])]
                return [summ,min(root.val,left[1]),max(root.val,right[2])]
                """if it is valid we'll use the max of the right min and the current val since in our bsae case
                    we used a very large number to be the smaller of the right and very small number to be larger
                    of the left"""
            
            return [max(left[0],right[0]),float('-inf'),float('inf')]
            """since child is invalid parent is also invalid so we make the min on the right very small number
                and max on the left very large number so it stays invalidated"""

        helper(root)
        res = max(ans)

        return res if res > 0 else 0