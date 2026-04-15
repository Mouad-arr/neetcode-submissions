# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if ( p == None and q != None ) or ( p!=None and q == None) :
            return False
        if q == None and p == None :
            return True
        if q.val != p.val :
            return False
        right=self.isSameTree(p.right,q.right)
        left=self.isSameTree(p.left,q.left)
        if not right or not left :
            return False
        return True