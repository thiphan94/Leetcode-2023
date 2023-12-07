# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_value = 10**5
        previous = -1

        def dfs(node):
            nonlocal min_value, previous
            if not node:
                return
            dfs(node.left)
            current_node = node.val
            if previous != -1:
                diff_value = current_node - previous
                min_value = min(min_value, diff_value)
            previous = current_node
            dfs(node.right)

        dfs(root)
        return min_value
