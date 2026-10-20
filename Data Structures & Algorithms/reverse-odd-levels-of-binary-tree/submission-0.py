# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque()
        q.append(root)
        niv=0
        while len(q)!=0:
            if niv%2==1 :
                n=len(q)
                L=[0]*n
                for i in range(n):
                    node =q[i]
                    L[i]=node.val
                    if node.left:
                        q.append(node.left)
                        q.append(node.right)
                for i in range(n):
                    node=q.popleft()
                    node.val = L[n-i-1]
                niv+=1
            else:
                n=len(q)
                for _ in range(n):
                    node=q.popleft()
                    if node.left:
                        q.append(node.left)
                        q.append(node.right)
                niv+=1
        return root
        