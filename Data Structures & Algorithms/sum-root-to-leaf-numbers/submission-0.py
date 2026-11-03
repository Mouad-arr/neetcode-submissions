# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        som=0
        def dfs(node,cur):
            nonlocal som
            if not node :
                return 
            if not node.left and not node.right :
                som+=int(cur+str(node.val))
            else :
                dfs(node.left,cur+str(node.val))
                dfs(node.right,cur+str(node.val))
        dfs(root,"")
        return som