# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res=root
        def dfs(node):
            nonlocal res
            if node.val == q.val or node.val == p.val :
                if node.right and dfs(node.right):
                    res=node
                    return True
                if node.left and dfs(node.left) :
                    res=node
                    return True
                return True
            b1=node.left and dfs(node.left)
            b2=node.right and dfs(node.right)
            if b1 and b2 :
                res=node
                return True
            elif b1 or b2 :
                return True
            return False
        dfs(root)
        return res