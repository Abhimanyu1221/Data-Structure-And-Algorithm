from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Multi-source BFS
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        def canReach(limit):
            if dist[0][0] < limit:
                return False

            q = deque([(0,0)])
            visited = {(0,0)}

            while q:
                x, y = q.popleft()

                if (x, y) == (n-1, n-1):
                    return True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < n and
                        0 <= ny < n and
                        (nx, ny) not in visited and
                        dist[nx][ny] >= limit
                    ):
                        visited.add((nx, ny))
                        q.append((nx, ny))

            return False

        left = 0
        right = max(max(row) for row in dist)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if canReach(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans