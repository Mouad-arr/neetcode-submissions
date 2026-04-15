# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        L=[]
        def fct(root,L):
            if root:
                L.append(root.val)
            if root.right :
                L=fct(root.right,L)
            if root.left :
                L=fct(root.left,L)
            return L
        L=fct(root,L)
        L.sort()
        return L[k-1]