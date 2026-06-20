class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        # print(max)
        sum1=0
        for val in nums:
            sum1=sum1+val
            maximum = max(sum1,maximum)
            if sum1<0:
                sum1=0
        print(maximum)
        return maximum