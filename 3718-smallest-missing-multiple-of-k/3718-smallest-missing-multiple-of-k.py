class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num = set(nums)
        i=1
        while True:
            if i*k in num:
                i+=1
            else :
                return i*k
