# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q = deque()
        q.append(root)
        niveau=0
        while len(q)!=0:
            N=[]
            n=len(q)
            for _ in range(n):
                rot = q.popleft()
                if niveau %2==0:
                    N.append(rot.val)
                else:
                    N.insert(0,rot.val)
                if rot.left:
                    q.append(rot.left)
                if rot.right:
                    q.append(rot.right)
            niveau+=1
            res.append(N)
        return res