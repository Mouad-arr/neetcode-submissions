# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        if abs(self.height(root.right)-self.height(root.left)) > 1 :
            return False
        left= self.isBalanced(root.left)
        right=self.isBalanced(root.right)
        return left and right
    def height(self , root: Optional[TreeNode]) -> int :
        if not root :
            return 0
        return 1+max(self.height(root.left),self.height(root.right))