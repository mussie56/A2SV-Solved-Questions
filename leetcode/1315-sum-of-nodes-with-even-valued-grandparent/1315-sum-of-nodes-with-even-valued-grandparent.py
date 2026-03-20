# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.score = 0
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        # score = 0
        def helper(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return [0,0]
            left = helper(root.left)
            right = helper(root.right)

            if not root.val%2:
                self.score+=left[1]+right[1]
                # print(self.score)

            return [root.val,left[0]+right[0]]

        val,summ = helper(root)

        return self.score