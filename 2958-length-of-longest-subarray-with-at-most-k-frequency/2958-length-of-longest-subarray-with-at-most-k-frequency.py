class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] in freq:
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            length = right - left + 1

            if length > ans:
                ans = length

        return ans