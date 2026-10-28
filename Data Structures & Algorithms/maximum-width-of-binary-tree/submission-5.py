# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        mx = 0

        while q:
            n = len(q)
            first = q[0][1]
            last = 0

            for _ in range(n):
                node, idx = q.popleft()
                idx -= first
                last = idx

                if node.left:
                    q.append((node.left, 2 * idx))

                if node.right:
                    q.append((node.right, 2 * idx + 1))

            mx = max(mx, last + 1)

        return mx