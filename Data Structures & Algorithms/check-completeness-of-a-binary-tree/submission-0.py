# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q=deque([root])
        level=0
        while len(q)!=0:
            n=len(q)
            if n==pow(2,level):
                good=True
                for _ in range(n):
                    node=q.popleft()
                    if node.left:
                        if good:
                            q.append(node.left)
                        else :
                            return False
                    else:
                        good=False
                    if node.right:
                        if good:
                            q.append(node.right)
                        else:
                            return False
                    else :
                        good=False
                level+=1
            else :
                for _ in range(n):
                    node=q.popleft()
                    if node.left or node.right :
                        return False
        return True