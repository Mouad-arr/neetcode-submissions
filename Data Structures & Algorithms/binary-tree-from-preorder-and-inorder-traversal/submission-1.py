# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if len(preorder)==0 :
                return None
            if len(preorder) == 1 :
                return TreeNode(preorder[0])
            racine=TreeNode(preorder[0])
            index=inorder.index(preorder[0])

            inorder_left=inorder[0:index]
            inorder_right=inorder[index+1:]

            preorder_left=preorder[1:len(inorder_left)+1]
            preorder_right=preorder[len(inorder_left)+1:]

            racine.left = self.buildTree( preorder_left,inorder_left)
            racine.right = self.buildTree( preorder_right,inorder_right)

            return racine

