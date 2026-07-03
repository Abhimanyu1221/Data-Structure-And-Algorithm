from collections import deque
from typing import List
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        maxEdge = 0

        # Build graph
        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            maxEdge = max(maxEdge, w)

        # Topological Sort
        q = deque()
        topo = []

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            topo.append(node)

            for nxt, _ in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        # Check if score >= limit is possible
        def can(limit):
            INF = float('inf')
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue

                # Intermediate offline nodes are not allowed
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue

                    if v != n - 1 and v != 0 and not online[v]:
                        continue

                    dp[v] = min(dp[v], dp[u] + w)

            return dp[n - 1] <= k

        left = 0
        right = maxEdge
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans