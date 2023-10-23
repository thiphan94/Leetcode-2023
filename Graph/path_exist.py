from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        graph = [[] for i in range(n)]
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        visited = [False for _ in range(n)]
        stack = [source]

        while stack:
            key = stack.pop(0)
            visited[key] = True
            if destination in graph[key]:
                return True
            for elt in graph[key]:
                if not visited[elt]:
                    stack.append(elt)
        return False
