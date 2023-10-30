from typing import List


from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0

        adj_list = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    adj_list[i + 1].append(j + 1)

        visited = set()

        for i in range(len(isConnected)):
            node = i + 1
            if node in visited:
                continue
            stack = [node]
            while stack:
                currNode = stack.pop()

                for child in adj_list[currNode]:
                    if child not in visited:
                        visited.add(child)
                        stack.append(child)

            count += 1
        return count
