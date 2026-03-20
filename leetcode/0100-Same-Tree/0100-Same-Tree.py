# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(root: Optional[TreeNode]) -> List[int]:
            if root:
                arr = [root.val]
                left = inorder(root.left)
                arr = left+arr
                right = inorder(root.right)
                arr = arr+right
                return arr
            return [None]

        def preorder(root: Optional[TreeNode]) -> List[int]:
            if root:
                left = preorder(root.left)
                arr = [root.val]+left
                right = preorder(root.right)
                arr = arr+right
                return arr
            return [None]
            
        inp = inorder(p)
        prep = preorder(p)
        inq = inorder(q)
        preq = preorder(q)
        return inp == inq and prep == preq