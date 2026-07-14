from math import gcd
from functools import lru_cache

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        @lru_cache(None)
        def dfs(i, g1, g2):
            if i == n:
                return 1 if g1 == g2 and g1 != 0 else 0

            x = nums[i]

            ans = dfs(i + 1, g1, g2)

            ng1 = x if g1 == 0 else gcd(g1, x)
            ans += dfs(i + 1, ng1, g2)

            ng2 = x if g2 == 0 else gcd(g2, x)
            ans += dfs(i + 1, g1, ng2)

            return ans % MOD

        return dfs(0, 0, 0)