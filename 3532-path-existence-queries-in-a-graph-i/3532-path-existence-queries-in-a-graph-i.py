from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        comp = [0] * n

        component = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                component += 1

            comp[i] = component

        ans = []

        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans