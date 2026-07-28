class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        
        left_half = []
        middle = ""
        
        for ch in sorted(count.keys()):
            c = count[ch]
            if c % 2 == 1:
                middle = ch
            left_half.append(ch * (c // 2))
        
        left_half = "".join(left_half)
        return left_half + middle + left_half[::-1]