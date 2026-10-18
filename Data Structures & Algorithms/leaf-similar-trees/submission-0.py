# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1=[]
        leafs2=[]
        def dfs1(node):
            if not node :
                return 
            if not node.left and not node.right :
                leafs1.append(node.val)
                return
            dfs1(node.left)
            dfs1(node.right) 
        def dfs2(node):
            if not node :
                return 
            if not node.left and not node.right :
                leafs2.append(node.val)
                return
            dfs2(node.left)
            dfs2(node.right) 
        dfs1(root1)
        dfs2(root2)
        if len(leafs1)!=len(leafs2):
            return False
        for i in range(len(leafs1)):
            if leafs1[i]!=leafs2[i]:
                return False
        return True