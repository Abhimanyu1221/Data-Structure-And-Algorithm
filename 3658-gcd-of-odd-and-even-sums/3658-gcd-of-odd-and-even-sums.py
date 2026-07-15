class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=1
        even=2
        oddsum=0
        evensum=0
        for i in range(n):
            oddsum = oddsum+odd
            evensum=evensum+even
            even=even+2
            odd=odd+2
        while evensum:
            oddsum,evensum=evensum,oddsum%evensum
        return oddsum
