# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        k = 0

        def dfs(node):
            nonlocal k
            if not node:
                return 0, 0

            l_sub, l_nbr = dfs(node.left)
            r_sub, r_nbr = dfs(node.right)
            sum_value = node.val + l_sub + r_sub
            nbr_node = 1 + l_nbr + r_nbr
            print(node.val, sum_value, nbr_node, k)
            if sum_value // nbr_node == node.val:
                k += 1
            return sum_value, nbr_node

        dfs(root)
        return k
