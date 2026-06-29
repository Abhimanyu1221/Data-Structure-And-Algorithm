class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s1 = sum(nums)
        cur=0
        ans=[]
        for i in range(0,len(nums)):
            lsum=cur
            cur = cur+nums[i]
            rsum=s1-cur
            ans.append(abs(rsum-lsum))
        return ans
