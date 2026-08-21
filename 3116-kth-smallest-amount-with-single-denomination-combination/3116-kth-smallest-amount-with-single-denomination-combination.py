class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []

        for mask in range(1, 1 << n):
            cur_lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    cur_lcm = math.lcm(cur_lcm, coins[i])

            sign = 1 if bits & 1 else -1
            subsets.append((cur_lcm, sign))

        def count(x):
            total = 0

            for lcm, sign in subsets:
                if lcm <= x:
                    total += sign * (x // lcm)

            return total

        left = 1
        right = k * min(coins)

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left