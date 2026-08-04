class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        MIN = min(nums)
        MAX = max(nums)
        result = []
        for i in range(MIN,MAX):
            if i not in nums:
                result.append(i)
        return result