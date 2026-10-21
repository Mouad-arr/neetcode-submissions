# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        op = 0

        while q:
            n = len(q)
            L = []

            for _ in range(n):
                node = q.popleft()
                L.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            S = sorted(L)
            pos = {val: i for i, val in enumerate(S)}

            for i in range(n):
                while L[i] != S[i]:
                    j = pos[L[i]]

                    L[i], L[j] = L[j], L[i]
                    op += 1

        return op