class Solution:
    def findGCD(self, nums: List[int]) -> int:
       a=float('inf')
       b=float('-inf')
       for  num in nums:
            if num > b:
                b = num
            if num < a:
                a = num
       while b:
            a,b = b, a%b
       return a
