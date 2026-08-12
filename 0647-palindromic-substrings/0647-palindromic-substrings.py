class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def checkpalindrom(left,right)->int:
            palindromcount = 0
            while left>=0 and right <len(s) and s[left] == s[right]:
                palindromcount +=1
                left -=1
                right+=1
            return palindromcount
        

        for i in range(len(s)):
            count+=checkpalindrom(i,i)
            count+=checkpalindrom(i,i+1)
        return count