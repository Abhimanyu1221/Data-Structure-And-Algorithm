class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        j=0
        max_size =0

        for i in range(len(s)):
            while s[i] in unique:
                unique.remove(s[j])
                j+=1
            unique.add(s[i])
            max_size = max(max_size,i-j+1)
        return max_size