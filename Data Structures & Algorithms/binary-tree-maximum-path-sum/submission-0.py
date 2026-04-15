# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def getMax(root):
            if not root :
                return 0
            left=getMax(root.left)
            right=getMax(root.right)
            return max(0,root.val+max(right,left))
        def pathNode(root) :
            m=root.val
            return m + getMax(root.right) + getMax(root.left)
        queue=deque([root])
        m=-float('inf')
        while len(queue)!=0 :
            node=queue.popleft()
            m=max(m,pathNode(node))
            if node.right :
                queue.append(node.right)
            if node.left :
                queue.append(node.left)
        return m