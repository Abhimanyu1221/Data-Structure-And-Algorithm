from typing import List

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return 0

        n = len(nums)
        bit = BIT(2 * n + 1)

        s = n + 1
        bit.update(s, 1)

        ans = 0

        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            ans += bit.query(s - 1)
            bit.update(s, 1)

        return ans