# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pref = {0:1}
        self.count = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(root: Optional[TreeNode],summ: int,targetSum: int) -> None:
            if not root:
                return
            summ+=root.val
            if summ-targetSum in self.pref:
                self.count+=self.pref[summ-targetSum]
            self.pref[summ] = self.pref.get(summ,0)+1

            helper(root.left,summ,targetSum)
            helper(root.right,summ,targetSum)
            self.pref[summ] -= 1
            return 
        helper(root,0,targetSum)
        return self.count