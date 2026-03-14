class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        val  = num-((9)*((num-1)//(9)))
        print(val)
        return val