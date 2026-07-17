from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)


        freq = [0] * (max_val + 1)

        for num in nums:
            freq[num] += 1


        exact = [0] * (max_val + 1)

        for g in range(max_val, 0, -1):


            count = 0

            for multiple in range(g, max_val + 1, g):
                count += freq[multiple]


            pairs = count * (count - 1) // 2


            for multiple in range(2 * g, max_val + 1, g):
                pairs -= exact[multiple]

            exact[g] = pairs

        prefix = [0] * (max_val + 1)

        for g in range(1, max_val + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        answer = []

        for query in queries:
            left = 1
            right = max_val

            while left < right:
                mid = (left + right) // 2

                if prefix[mid] > query:
                    right = mid
                else:
                    left = mid + 1

            answer.append(left)

        return answer