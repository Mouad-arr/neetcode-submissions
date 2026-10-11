# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        mergedTree = TreeNode()
        if root1==None and root2==None :
            return None
        elif root1==None :
            mergedTree.val = root2.val
            mergedTree.left = root2.left
            mergedTree.right = root2.right
        elif root2==None :
            mergedTree.val = root1.val
            mergedTree.left = root1.left
            mergedTree.right = root1.right
        else:
            mergedTree.val = root1.val + root2.val
            mergedTree.left = self.mergeTrees(root1.left,root2.left)
            mergedTree.right = self.mergeTrees(root1.right,root2.right)
        return mergedTree