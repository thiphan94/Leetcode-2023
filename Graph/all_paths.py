from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # # Mark the current node as visited and store in path
        s = 0

        target = len(graph) - 1
        paths, targets = [[s]], []
        # print(paths, targets)
        while paths:
            node = paths.pop(s)
            # print(node)
            edges = graph[node[-1]]
            # print(edges)
            if not edges:
                continue
            for edge in edges:
                if edge == target:
                    targets.append(node + [edge])
                else:
                    paths = [node + [edge]] + paths
                    # print("paths", paths)
        return targets
