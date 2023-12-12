from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            nonlocal res
            if not node:
                return None
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            return res

        return dfs(root)
