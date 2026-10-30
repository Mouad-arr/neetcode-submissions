class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n=len(preorder)
        if n==0:
            return None
        root=TreeNode(preorder[0])
        if n==1:
            return root
        i=0
        while i<n and postorder[i]!=preorder[1]:
            i+=1
        i+=1
        root.left=self.constructFromPrePost(preorder[1:i+1],postorder[:i])
        root.right=self.constructFromPrePost(preorder[i+1:],postorder[i:-1])
        return root