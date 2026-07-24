class Solution:
    def uniqueXorTriplets(self, nums):
        values = set(nums)

        pair = [False] * 2048

        for a in values:
            for b in values:
                pair[a ^ b] = True

        result = [False] * 2048

        for x in range(2048):
            if pair[x]:
                for c in values:
                    result[x ^ c] = True

        return sum(result)