class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for pos,num in enumerate(nums):
            val=target-num
            # print(dict1)
            if val in dict1:
                return(pos,dict1.get(val))
            dict1[num]=pos