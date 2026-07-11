from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        def dfs(node):
            visited[node] = True

            vertices = 1
            degreeSum = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    v, d = dfs(nei)
                    vertices += v
                    degreeSum += d

            return vertices, degreeSum

        for i in range(n):

            if not visited[i]:

                vertices, degreeSum = dfs(i)

                edgeCount = degreeSum // 2

                if edgeCount == vertices * (vertices - 1) // 2:
                    answer += 1

        return answer