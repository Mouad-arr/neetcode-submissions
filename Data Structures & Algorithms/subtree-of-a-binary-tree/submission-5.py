# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if  not subRoot  :
            return True
        if not root :
            return False
        if root.val == subRoot.val :
            if ( root.right and not subRoot.right ) or (root.left and not subRoot.left) or  (not root.right and  subRoot.right ) or ( not root.left and  subRoot.left)  :
                return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right,subRoot)
            elif self.isEqual(root,subRoot) :
                return True
            else :
                return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right,subRoot)
        elif root.left or root.right :
            return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right,subRoot)
        return False
    def isEqual(self , root:Optional[TreeNode] , subRoot : Optional[TreeNode]) -> bool :
        if not root and not subRoot :
            return True
        elif not root or not subRoot :
            return False
        elif root.val != subRoot.val :
            return False
        else:
            return self.isEqual(root.right,subRoot.right) and self.isEqual(root.left,subRoot.left)