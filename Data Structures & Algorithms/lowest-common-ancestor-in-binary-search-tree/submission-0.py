# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not q or not p:
            return None
        # if p.left.val = q.val or p.right.vl=q.val :
        #     return p
        # elif q.left.val = p.val or q.right.val=q.val :
        #     return q
        if min(q.val,p.val) <= root.val and max(q.val,p.val) >= root.val :
            return root
        if q.val < root.val and p.val < root.val :
            return self.lowestCommonAncestor(root.left,p,q)
        elif q.val > root.val and p.val > root.val :
            return self.lowestCommonAncestor(root.right,p,q)