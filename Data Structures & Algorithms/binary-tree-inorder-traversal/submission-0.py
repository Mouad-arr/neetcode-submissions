# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur=root
        res=[]
        if cur==None:
            return res
        def dfs(cur):
            if cur.left!=None:
                dfs(cur.left)
            res.append(cur.val)
            if cur.right!=None:
                dfs(cur.right)
            return
        dfs(cur)
        return res