from math import gcd
from typing import List
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefix_gcd.append(gcd(num, mx))

        prefix_gcd.sort()

        ans = 0
        i = 0
        j = len(prefix_gcd) - 1

        while i < j:
            ans += gcd(prefix_gcd[i], prefix_gcd[j])
            i += 1
            j -= 1

        return ans