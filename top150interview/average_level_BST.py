from collections import defaultdict
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        elements = defaultdict(list)

        def dfs(node, level):
            nonlocal elements
            if not node:
                return
            elements[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return [sum(items) / len(items) for (level, items) in elements.items()]
