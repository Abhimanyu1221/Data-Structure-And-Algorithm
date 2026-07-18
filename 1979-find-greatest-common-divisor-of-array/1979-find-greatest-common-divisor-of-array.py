class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        # print(small)
        b = max(nums)
        # print(largest)
        while b:
            a,b = b,a%b
        return a