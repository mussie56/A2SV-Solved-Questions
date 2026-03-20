# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def inorder(root: Optional[TreeNode]) -> List[int]:
            if root:
                arr = [str(root.val)]
                left = inorder(root.left)
                arr = left+arr
                right = inorder(root.right)
                arr = arr+right
                return arr
            return ["None"]

        def preorder(root: Optional[TreeNode]) -> List[int]:
            if root:
                left = preorder(root.left)
                arr = [str(root.val)]+left
                right = preorder(root.right)
                arr = arr+right
                return arr
            return ["None"]

        treein = inorder(root)
        treepre = preorder(root)
        subin = inorder(subRoot)
        subpre = preorder(subRoot)

        return "".join(subin) in "".join(treein) and "".join(subpre) in "".join(treepre)