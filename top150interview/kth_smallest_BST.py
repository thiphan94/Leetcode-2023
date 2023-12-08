# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            if not node:
                return
            dfs(node.left)
            k -= 1
            if k == 0:
                self.val = node.val
            dfs(node.right)

        dfs(root)
        return self.val
